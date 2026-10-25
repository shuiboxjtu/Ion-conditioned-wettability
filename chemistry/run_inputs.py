"""Run retained PHREEQC inputs in isolated output directories (Python 3)."""
import argparse
import csv
import hashlib
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
HISTORICAL_DATABASE_SHA256 = '2cfa5be85bd29bd7556946a0b7f104857ff848d04b18c9f57e9d2508195e72fe'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phreeqc', default='phreeqc', help='PHREEQC command-line executable')
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--stem', help='One input stem; default: all inputs in scenario_manifest.csv')
    parser.add_argument('--output', type=Path, default=ROOT / 'generated')
    parser.add_argument('--allow-alternative-database', action='store_true', help='Explicitly allow a database different from the historical GeoChem.dat')
    args = parser.parse_args()
    database = args.database.resolve(strict=True)
    digest = hashlib.sha256(database.read_bytes()).hexdigest()
    if digest != HISTORICAL_DATABASE_SHA256 and not args.allow_alternative_database:
        parser.error('Database differs from historical GeoChem.dat. Use the original database, or explicitly use --allow-alternative-database for a new calculation, not an exact reproduction.')
    executable = shutil.which(args.phreeqc)
    if not executable:
        parser.error('PHREEQC executable not found; build/install PHREEQC first.')
    with (ROOT / 'scenario_manifest.csv').open(encoding='utf-8-sig', newline='') as stream:
        stems = [row['stem'] for row in csv.DictReader(stream)]
    if args.stem:
        if args.stem not in stems:
            parser.error('Unknown input stem')
        stems = [args.stem]
    for stem in stems:
        destination = args.output.resolve() / stem
        destination.mkdir(parents=True, exist_ok=True)
        if any(destination.iterdir()):
            parser.error(f'Output directory is not empty: {destination}; choose a new --output directory')
        source = ROOT / 'inputs' / (stem + '.pqi')
        result = subprocess.run([executable, str(source), str(destination / 'phreeqc.out'), str(database)], cwd=destination, capture_output=True, text=True)
        (destination / 'console.log').write_text(result.stdout + result.stderr, encoding='utf-8')
        (destination / 'database_sha256.txt').write_text(digest + '\n', encoding='ascii')
        report = destination / 'phreeqc.out'
        content = report.read_text(errors='replace') if report.exists() else ''
        if result.returncode or any(marker in content.lower() for marker in ('error:', 'failed to converge', 'did not converge')):
            raise RuntimeError(f'PHREEQC failed for {stem}; inspect {destination}')
        print(stem)

if __name__ == '__main__':
    main()
