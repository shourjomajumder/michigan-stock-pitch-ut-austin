const sleep=ms=>new Promise(r=>setTimeout(r,ms));
for(let i=0;i<20&&![...document.querySelectorAll('li')].some(l=>/[A-Z]{3}–[A-Z]{3}/.test(l.innerText));i++)await sleep(1000);
const parse=()=>{const out={};for(const l of document.querySelectorAll('li')){const a=l.innerText.split('\n').map(s=>s.trim()).filter(Boolean);const rt=a.find(s=>/^[A-Z]{3}–[A-Z]{3}$/.test(s));if(!rt)continue;const al=(a[a.indexOf('–')+2]||'');const stop=a.find(s=>/Nonstop|stop/.test(s));const i=a.indexOf(stop);const bags=a.slice(i).filter(s=>/^\d$/.test(s)).join('/');const pr=a.filter(s=>/^\$[\d,]+$/.test(s)).map(s=>+s.replace(/[$,]/g,''));if(!pr.length)continue;const p=Math.min(...pr);const k=al+'|'+rt+'|'+stop;if(!(k in out)||out[k].p>p)out[k]={p,bags};}return out;};
const b=parse();const t=[...document.querySelectorAll('[role=tab]')].find(e=>/Cheapest/.test(e.innerText));if(t){t.click();await sleep(4500);}const c=parse();
const m={};for(const [k,v] of Object.entries(b))m[k]={best:v.p,ch:null,bags:v.bags};for(const [k,v] of Object.entries(c)){m[k]=m[k]||{best:null,bags:v.bags};m[k].ch=v.p;}
const f=Object.fromEntries(Object.entries(m).filter(([k])=>/JetBlue|United/.test(k)));
JSON.stringify({d:[...document.querySelectorAll('input')].map(i=>i.value).filter(Boolean).slice(-2).join('|'),blocked:/unusual traffic|captcha/i.test(document.body.innerText),f})
