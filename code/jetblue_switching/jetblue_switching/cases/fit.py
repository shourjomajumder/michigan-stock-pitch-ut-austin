import numpy as np
cases=[('Delta vs JetBlue, BOS 2015-19',0,-4.0),('Delta vs Alaska, SEA 2015-19',0,0.8),('Delta vs Alaska, SEA 2019-25',0,-1.1),('Delta vs American, LAX 2023-25',0,-1.4),
('USAir/BA: United',2,15),('USAir/BA: Delta',2,12),('USAir/BA: Northwest',2,9),('USAir/BA: TWA',2,6),('USAir/BA: Continental',2,5),('USAir/BA: interior-city rival',2,11),
('Delta/WestJet: United',2,4.8),('Delta/WestJet: American',2,6.8),('Delta/Virgin JV: other carriers',3,-1.0)]
x=np.array([c[1] for c in cases]);y=np.array([c[2] for c in cases])
for lab,m in [('all',x>=0),('0-2',x<=2)]:
  b=np.polyfit(x[m],y[m],1);r=np.corrcoef(x[m],y[m])[0,1];print(lab,m.sum(),b,r,np.polyval(b,1))
print('means',{k:y[x==k].mean() for k in set(x)})
m=x<=2;b=np.polyfit(x[m],y[m],1);res=y[m]-np.polyval(b,x[m]);sd=res.std(ddof=2);print('sd',sd)
p=np.polyval(b,1);h=22/12;print('cum',p*h,(p-sd)*h,(p+sd)*h)
# standard error of mean prediction at x=1
n=m.sum();xm=x[m].mean();se=sd*np.sqrt(1/n+(1-xm)**2/((x[m]-xm)**2).sum());print('se',se,(p+1.96*se)*h,(p-1.96*se)*h)
