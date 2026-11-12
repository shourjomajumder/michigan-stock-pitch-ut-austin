# Michigan Stock Pitch UT Austin

The data and calculations behind our pair-trade pitch: long Frontier Group Holdings (ULCC), short JetBlue Airways (JBLU), hedged with $1.16 of JBLU short for every $1 of ULCC long. `data/` holds the data by topic (flights and fares, air traffic from DOT/BTS, stock prices, hedge and macro risk, SEC filings, Frontier routes and load factor, JetBlue switching cases, New York and JFK, company and industry facts, valuation inputs), each with a SOURCES file, and `code/` holds the scripts used for the calculations, in matching folders. `DATA_INDEX.md` lists every file. Bloomberg data, broker reports and the Excel valuation models are not included. Commit dates are the dates the data was pulled, taken from the original files.










Full raw source files (about 10 GB of BTS on-time and DOT DB1B data, pulled 2026-11-11) are on Hugging Face: https://huggingface.co/datasets/shourjomajumder/michigan-stock-pitch-raw-data
