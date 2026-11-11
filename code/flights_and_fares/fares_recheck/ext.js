(async()=>{const sl=ms=>new Promise(r=>setTimeout(r,ms));for(let i=0;i<24&&![...document.querySelectorAll('li')].some(l=>/Nonstop/.test(l.innerText));i++)await sl(500);
const b=[...document.querySelectorAll('button')].find(x=>/more flights/i.test(x.innerText));if(b){b.click();await sl(2500);}
const rows=[...document.querySelectorAll('li')].map(l=>l.innerText.split(/\n+/).map(s=>s.trim()).filter(Boolean)).filter(a=>a.includes('Nonstop')&&a.some(s=>/^\$[\d,]+$/.test(s)));
const out=[];for(const a of rows){const ap=a.find(s=>/^[A-Z]{3}–[A-Z]{3}$/.test(s));const al=a[a.indexOf(ap)-2];const p=+a.find(s=>/^\$[\d,]+$/.test(s)).slice(1).replace(',','');const bi=a.indexOf(a.find(s=>/emissions/.test(s)));const bags=bi>=0?a.slice(bi+1,bi+3).join('/'):'';out.push([al,ap,p,bags,a[0]]);}
const ins=[...document.querySelectorAll('input')].map(i=>i.value).filter(Boolean).join(' ; ');return JSON.stringify({url:location.href.slice(46,140),ins,n:rows.length,ts:new Date().toISOString(),out});})()
