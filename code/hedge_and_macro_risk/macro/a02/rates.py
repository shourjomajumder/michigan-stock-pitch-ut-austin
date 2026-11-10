H=1.163
# $m. Sources in a02.md
U=dict(px=7.49,sh=230.4176,debt=486,cash=976,liq=1196,intexp9m=34,flt=320,flt_hi=386,m27=102,m28=39,
       ebitda9m=-488+177,rent9m=832,cash_inc_per100=9.76)
J=dict(px=3.16,sh=377.3,debt=8393,cash=1626,liq=2200,intexp9m=440,flt=2000,flt_hi=3520,m27=477,m28=582,
       ebitda9m=-509+548,rent9m=49,cash_inc_per100=16)
res={}
for n,d in (('ULCC',U),('JBLU',J)):
    mc=d['px']*d['sh']; ebitdar=(d['ebitda9m']+d['rent9m'])*4/3
    fl=d['flt']*0.01; fl_hi=d['flt_hi']*0.01; net=fl-d['cash_inc_per100']
    refi=d['m27']+d['m28']; r1=refi*0.01; r2=refi*0.02
    res[n]=dict(mc=mc,ebitdar=ebitdar,nd_ebitdar=(d['debt']-d['cash'])/ebitdar,fl=fl,fl_hi=fl_hi,net=net,r1=r1,r2=r2,
       tot1=fl+r1,tot2=fl+r2)
    print(n,f"mcap {mc:.0f} EBITDAR(ann9M) {ebitdar:.0f} netdebt/EBITDAR {(d['debt']-d['cash'])/ebitdar:.2f} "
          f"float+100 {fl:.1f} (hi {fl_hi:.1f}, net of cash income {net:.1f}) refi+100 {r1:.1f} refi+200 {r2:.1f} "
          f"| %mcap: fl {fl/mc:.2%} hi {fl_hi/mc:.2%} r1 {r1/mc:.2%} r2 {r2/mc:.2%} tot+100 {(fl+r1)/mc:.2%} tot+200 {(fl+r2)/mc:.2%}")
for k in ('fl','fl_hi','net','r1','r2','tot1','tot2'):
    u=res['ULCC'][k]/res['ULCC']['mc']; j=res['JBLU'][k]/res['JBLU']['mc']
    print(k,f"ULCC {u:.3%} JBLU {j:.3%} pair(ULCC-1.163*JBLU) {(-u)-H*(-j):+.3%} per $1 long ULCC (earnings-yield terms)")
