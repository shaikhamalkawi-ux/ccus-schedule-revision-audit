#!/usr/bin/env python3
"""Supplementary S86 cutoff-crossing audit from a previously admitted IEA cohort.

Non-causal; no interpolation of missing years/capacity; no third-party raw input is
redistributed. Use the same fixed 2025 capacity and function partition as the
matched 2025--2026 same-definition analysis.
"""
import csv
import json
import argparse
from decimal import Decimal
from pathlib import Path
from collections import Counter

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--input',required=True,type=Path,help='Previously admitted same-ID / same-status 2025-2026 cohort CSV')
parser.add_argument('--output-dir',required=True,type=Path,help='Where to put aggregate-only outputs')
parser.add_argument('--check-study-anchors',action='store_true',help='Assert R4.2 known 461-cohort values')
args=parser.parse_args()
INPUT=args.input
OUT=args.output_dir
OUT.mkdir(parents=True,exist_ok=True)
PORTFOLIOS={'Capture':{'capture','ccu','full chain'},'Storage':{'storage','t&s','full chain'}}
FIELDS=['function','cutoff_year','margin_years','capacity_known_records','baseline_2025_MtCO2yr','endpoint_2026_MtCO2yr','exits_n','gross_exit_MtCO2yr','entries_n','gross_entry_MtCO2yr','net_delta_MtCO2yr','pct_change','top3_exit_share_pct']
with INPUT.open(newline='',encoding='utf-8-sig') as fh:
 records=list(csv.DictReader(fh))
if args.check_study_anchors: assert len(records)==461, 'Unexpected 2025--2026 matched cohort size'
assert len({r['ID'] for r in records})==len(records), 'Duplicate IDs'
assert {r['Status'] for r in records} <= {'Planned','Under construction'}
if args.check_study_anchors:
 assert sum(int(Decimal(r['Operation_2026']))>int(Decimal(r['Operation_2025'])) for r in records)==138
 assert sum(int(Decimal(r['Operation_2026']))<int(Decimal(r['Operation_2025'])) for r in records)==7

rows=[]
for fname,types in PORTFOLIOS.items():
 a=[]
 for r in records:
  if r['Project_type_2025'].strip().lower() not in types or not r['IEA_est_capacity_2025'].strip():continue
  c=Decimal(r['IEA_est_capacity_2025'])
  assert c.is_finite() and c>=0
  a.append((r,int(Decimal(r['Operation_2025'])),int(Decimal(r['Operation_2026'])),c))
 for margin in range(4):
  cutoff=2030-margin
  before=sum((c for r,y0,y1,c in a if y0<=cutoff), Decimal(0))
  after=sum((c for r,y0,y1,c in a if y1<=cutoff), Decimal(0))
  exits=sorted([(r,y0,y1,c) for r,y0,y1,c in a if y0<=cutoff<y1],key=lambda x:x[3],reverse=True)
  entries=[(r,y0,y1,c) for r,y0,y1,c in a if y1<=cutoff<y0]
  gross_out=sum((c for r,y0,y1,c in exits),Decimal(0));gross_in=sum((c for r,y0,y1,c in entries),Decimal(0))
  assert after-before==gross_in-gross_out, f'Failed mass closure: {fname}, {cutoff}'
  top=sum((c for r,y0,y1,c in exits[:3]),Decimal(0))
  share=top/gross_out*100 if gross_out>0 else None
  row={'function':fname,'cutoff_year':cutoff,'margin_years':margin,'capacity_known_records':len(a),
       'baseline_2025_MtCO2yr':f'{before:.3f}','endpoint_2026_MtCO2yr':f'{after:.3f}',
       'exits_n':len(exits),'gross_exit_MtCO2yr':f'{gross_out:.3f}',
       'entries_n':len(entries),'gross_entry_MtCO2yr':f'{gross_in:.3f}',
       'net_delta_MtCO2yr':f'{after-before:+.3f}',
       'pct_change':f'{(after-before)/before*100:+.3f}' if before else 'NA',
       'top3_exit_share_pct':f'{share:.1f}' if share is not None else 'NA'}
  rows.append(row)
expected={('Capture',2030):('295.540','280.530','-15.010'),('Capture',2029):('196.687','180.306','-16.381'),
          ('Capture',2028):('168.255','137.968','-30.287'),('Capture',2027):('116.804','64.811','-51.993'),
          ('Storage',2030):('547.092','519.492','-27.600'),('Storage',2029):('330.444','301.744','-28.700'),
          ('Storage',2028):('287.244','273.794','-13.450'),('Storage',2027):('203.104','131.104','-72.000')}
if args.check_study_anchors:
 for r in rows:
  actual=(r['baseline_2025_MtCO2yr'],r['endpoint_2026_MtCO2yr'],r['net_delta_MtCO2yr'])
  assert actual==expected[(r['function'],r['cutoff_year'])],(r,actual)
 assert [(x['cutoff_year'],x['exits_n'],x['entries_n']) for x in rows if x['function']=='Storage']==[(2030,5,1),(2029,6,1),(2028,8,0),(2027,21,0)]
with (OUT/'S86_cutoff_crossing_summary.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=FIELDS,lineterminator='\n');w.writeheader();w.writerows(rows)
checks={'status':'PASS','source':'R4.2 admitted 2025--2026 matched cohort (461 unique IDs)','cohort_rows':len(records),'analysis_rows':len(rows),
 'capacity_subset':{name:len([x for x in records if x['Project_type_2025'].strip().lower() in types and x['IEA_est_capacity_2025'].strip()]) for name,types in PORTFOLIOS.items()},'checked_fixed_baseline_cutoffs':len(rows),'closure_failures':0,
 'claim_boundary':'source-report year-field update only; no physical delay or realized CO2 loss'}
(OUT/'S86_QA.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print('PASS',json.dumps(checks))
for r in rows: print(' | '.join(str(r[z]) for z in ('function','cutoff_year','exits_n','entries_n','gross_exit_MtCO2yr','gross_entry_MtCO2yr','net_delta_MtCO2yr','pct_change','top3_exit_share_pct')))
