"""Pull the Thesis 1 (Blue Sky switching) rows out of the final JetBlue model workbook (our own model; only thesis rows,
no consensus columns). Usage: python code/pipeline/extract_thesis1_from_model.py <path/to/JBLU_Model_Valuation.xlsx>
(final model lives in the repo's model folder; original: rv/appx4/models_final/JBLU_Model_Valuation.xlsx)."""
import sys, csv, pathlib, openpyxl
ROOT = pathlib.Path(__file__).resolve().parents[2]
wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
rows = [('sheet', 'row', 'label', 'unit', 'c1', 'c2', 'c3', 'c4')]
A = wb['Assumptions']
for r in range(16, 22):
    rows.append(('Assumptions', r, A.cell(r, 1).value, A.cell(r, 2).value, A.cell(r, 3).value, None, None, None))
rows.append(('Assumptions', 14, A.cell(14, 1).value, A.cell(14, 2).value, A.cell(14, 3).value, None, None, None))
rows.append(('Assumptions', 25, A.cell(25, 1).value, A.cell(25, 2).value, A.cell(25, 3).value, None, None, None))
rows.append(('Assumptions', 7, A.cell(7, 1).value, A.cell(7, 2).value, A.cell(7, 3).value, None, None, None))
D = wb['DCF']
for r in [51, 53, 54, 55, 62, 63, 64, 65, 66, 67, 68]:
    rows.append(('DCF', r, D.cell(r, 1).value, D.cell(r, 2).value, *[D.cell(r, c).value for c in range(3, 7)]))
out = ROOT / 'processed/model/thesis1_model_rows.csv'
csv.writer(open(out, 'w', newline='')).writerows(rows)
for x in rows: print(x)
