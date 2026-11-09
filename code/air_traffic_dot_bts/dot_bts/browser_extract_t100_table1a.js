// Browser-side extraction used for this analysis (run in a Chrome tab on the BTS TranStats
// T-100 Domestic Segment (U.S. Carriers) download page, Nov 8 2026; container cannot reach transtats).
// URL: https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FIM&QO_fu146_anzr=Nv4%20Pn44vr45
// Latest available on page: "Latest Available Data: July 2026".
// Fields: DEPARTURES_PERFORMED, SEATS, PASSENGERS, UNIQUE_CARRIER, ORIGIN, DEST, AIRCRAFT_TYPE, YEAR, MONTH, CLASS
// One download per year 2019-2026, all months. Filter CLASS == 'F' (scheduled passenger service).
// Aggregation (both directions summed, route = JFK-X):
//   Q rows: hub(JFK, or EWR for west-coast X), X, carrier (B6/UA/DL/AA/AS, others -> OT), year, quarter: pax, seats, deps
//          (rows with < 3 departures in the quarter dropped to remove diversions/one-offs)
//   U rows: UA at JFK by X, year, month, aircraft type
//   T rows: B6 and UA all-airport monthly totals (system domestic)
// Outputs written to src/*.csv by copying the page text (page <main><pre> dump).

const URL0 = location.href;
async function unzipAll(buf){
  const dv=new DataView(buf), u8=new Uint8Array(buf); let eocd=-1;
  for(let i=u8.length-22;i>=0;i--){ if(dv.getUint32(i,true)===0x06054b50){eocd=i;break;} }
  const n=dv.getUint16(eocd+10,true); let p=dv.getUint32(eocd+16,true); const out=[];
  for(let k=0;k<n;k++){
    const meth=dv.getUint16(p+10,true), csz=dv.getUint32(p+20,true), nl=dv.getUint16(p+28,true),
          el=dv.getUint16(p+30,true), cl=dv.getUint16(p+32,true), lho=dv.getUint32(p+42,true);
    const name=new TextDecoder().decode(u8.slice(p+46,p+46+nl)); p+=46+nl+el+cl;
    if(/Documentation/i.test(name)) continue;
    const lnl=dv.getUint16(lho+26,true), lel=dv.getUint16(lho+28,true); const st=lho+30+lnl+lel;
    const data=u8.subarray(st,st+csz);
    const txt = meth===0 ? new TextDecoder().decode(data)
      : await new Response(new Blob([data]).stream().pipeThrough(new DecompressionStream('deflate-raw'))).text();
    out.push({name,txt});
  }
  return out;
}
async function getYear(yr){
  const html = await (await fetch(URL0,{credentials:'include'})).text();   // fresh GET each time (server session)
  const doc = new DOMParser().parseFromString(html,'text/html');
  const f = [...doc.forms].find(x=>x.querySelector('[name=cboYear]'));
  const fd = new FormData(f);
  for (const k of [...fd.keys()]) { const el=f.querySelector(`[name="${k}"]`); if(el && el.type==='checkbox') fd.delete(k); }
  ['DEPARTURES_PERFORMED','SEATS','PASSENGERS','UNIQUE_CARRIER','ORIGIN','DEST','AIRCRAFT_TYPE','YEAR','MONTH','CLASS','chkDownloadZip'].forEach(k=>fd.set(k,'on'));
  fd.set('cboYear',String(yr)); fd.set('cboPeriod','All'); fd.set('cboGeography','All'); fd.set('btnDownload','Download'); fd.delete('txtSearch');
  const r = await fetch(URL0,{method:'POST',body:fd,credentials:'include'});
  return (await unzipAll(await r.arrayBuffer()))[0].txt;
}
// agg(csv, yr) -> {Q,U,T} as described above (see header). Results cached in localStorage 't100_<yr>'.

// DOT Consumer Airfare Report Table 1a (airport-pair markets), Socrata dataset tfrh-tu9e on data.transportation.gov:
// GET https://data.transportation.gov/resource/tfrh-tu9e.json?$where=year >= '2019' AND (airport_1 in ('JFK','EWR') OR airport_2 in ('JFK','EWR'))&$limit=50000
// Latest quarter in dataset on Nov 8 2026: 2026 Q1. Kept: JFK-{LAX,SFO,SEA,LAS,SAN,PHX,SLC} and EWR-{LAX,SFO} all quarters (2020 excluded);
// JFK-{DEN,ORD,IAH} and JetBlue top JFK routes for 2025Q2-2026Q1 only.
