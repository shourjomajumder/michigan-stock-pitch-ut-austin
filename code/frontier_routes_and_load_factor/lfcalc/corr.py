exec(open('sncy.py').read().split("L10=np.log(1.1)")[0])
Y=P[(~P.bad)&(P.bad4==False)].dropna(subset=['dLF','gyield','gASM']); Y=Y[~((Y.firm=='ALGT')&(Y.q>='2026Q2'))]
print('panel n',len(Y),'corr(dLF,gyield)=%.2f corr(dLF,gASM)=%.2f corr(gyield,gFuel)=%.2f'%(Y.dLF.corr(Y.gyield),Y.dLF.corr(Y.gASM),Y.gyield.corr(Y.gFuel)))
for f in ['ULCC','ALGT','SNCY']:
    S=Y[Y.firm==f]; print(f,'corr(dLF,gyield)=%.2f corr(dLF,gASM)=%.2f n=%d'%(S.dLF.corr(S.gyield),S.dLF.corr(S.gASM),len(S)))
