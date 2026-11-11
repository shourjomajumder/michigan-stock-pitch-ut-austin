#!/bin/sh
# Rebuild processed/ from raw/ and rerun every script; printed output goes to pair_hedge/outputs/<script>.out
# (scripts resolve their own paths, so this works from any cwd)
set -e
cd "$(dirname "$0")"
mkdir -p outputs
python3 -W ignore build_inputs.py          > outputs/build_inputs.out
python3 -W ignore fuel_share_of_revenue.py > outputs/fuel_share_of_revenue.out
python3 -W ignore one_year_stock_chart.py && cp out/JBLU_1yr_stock_chart.png outputs/
for s in i1_weekly i1_index k2 k1 k1_hedge k3_fuel k4 a4_miss a5_corr a5_vol a5_fuelvol chart_series macro_exposure; do
  python3 -W ignore $s.py > outputs/$s.out
done
echo "done: $(ls outputs | wc -l) outputs"
