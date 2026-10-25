"""Export newly generated OpenFOAM waterSaturation records to stdout as CSV."""
import argparse
import csv
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('case', type=Path)
args = parser.parse_args()
records = {}
for path in sorted((args.case / 'postProcessing' / 'waterSaturation').glob('*/volFieldValue.dat')):
    for line in path.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        values = line.split()
        if len(values) != 2:
            raise ValueError(f'Expected time and volAverage(alpha.water): {path}: {line}')
        records[float(values[0])] = float(values[1])
if not records:
    parser.error('No generated waterSaturation/volFieldValue.dat records found')
writer = csv.writer(sys.stdout)
writer.writerow(['time_s', 'water_volume_fraction'])
writer.writerows(sorted(records.items()))
