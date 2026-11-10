# pair P&L per $1 long ULCC = r_long - 1.163 * r_JBLU
H=1.163
eps=[ # name, long proxy, r_long, r_jblu, basis
("2008 CY (ALGT proxy)","ALGT",0.511,0.203,"chartrow CY total return"),
("2009 CY (ALGT proxy)","ALGT",-0.029,-0.232,"chartrow CY"),
("2008-09 cum (ALGT proxy)","ALGT",1.511*0.971-1,1.203*0.768-1,"chartrow CY compounded"),
("2020 Mar (SAVE proxy)","SAVE",-0.547,-0.433,"Motley Fool / S&P GMI, March 2020"),
("2020 yr hi->lo (SAVE)","SAVE",7.2368/40.2765-1,6.86/21.56-1,"macrotrends 2020 high/low"),
("2020 yr hi->lo (ALGT)","ALGT",64.0139/182.908-1,6.86/21.56-1,"macrotrends 2020 high/low"),
("2022 CY (ULCC)","ULCC",-0.243,-0.545,"chartrow/macrotrends CY"),
("2022 hi->lo (ULCC)","ULCC",8.34/14.61-1,6.19/16.19-1,"macrotrends 2022 high/low"),
("2022 CY (ALGT)","ALGT",-0.636,-0.545,"chartrow CY"),
("2025 hi->lo (ULCC)","ULCC",2.79/10.26-1,3.425/8.09-1,"MarketBeat 52w range; macrotrends JBLU 2025"),
("2025 CY (ULCC)","ULCC",-0.338,-0.421,"chartrow CY"),
]
for n,p,rl,rj,s in eps: print(f"{n:28s} {rl:+.1%} {rj:+.1%} pair {rl-H*rj:+.1%}  [{s}]")
