#!/usr/bin/env bash
# One-time setup on a fresh Ubuntu Vultr server. Run from inside the project folder:  bash setup.sh
set -e
sudo apt-get update -y && sudo apt-get install -y python3-venv unzip
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install duckdb pandas pyyaml requests python-dotenv matplotlib
mkdir -p data/raw_dot output logs
[ -f .env ] || echo "SERPAPI_KEY=paste_your_key_here" > .env
# daily live snapshot at 6:15 am server time, weekly re-analysis Sunday 7:00
( crontab -l 2>/dev/null; \
  echo "15 6 * * * cd $PWD && .venv/bin/python collect_live.py >> logs/live.log 2>&1"; \
  echo "0 7 * * 0 cd $PWD && .venv/bin/python analyze.py >> logs/analyze.log 2>&1" ) | crontab -
echo "Done. Next: put your SerpApi key in .env, drop DOT zip files in data/raw_dot, then run ingest_dot.py and analyze.py"
