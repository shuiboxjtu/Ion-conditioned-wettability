# PHREEQC chemistry inputs

This directory supplies 128 retained PHREEQC input decks, each with 41 mixing states. `scenario_manifest.csv` describes the input scenarios and parameter perturbations; it is input metadata, not calculated results. `historical_run_record.json` records the historical hashes of the database, runner and library, not the identity of the newly downloaded upstream snapshot.

The decks explicitly define the reduced non-electrostatic calcite and acidic-oil surface reactions, log equilibrium constants, prescribed pH, site inventories, brine mixing compositions, selected-output precision and TBP expression. `pH_8.5__NaCl`, `pH_8.5__CaCl2`, `pH_8.5__MgCl2` and `pH_8.5__Na2SO4` are baseline input stems. The remaining inputs contain the retained sensitivity settings.

## Software and execution

Build the upstream PHREEQC source supplied in `../software` or install the USGS command-line PHREEQC version 3. The original run used an IPhreeqc-based runner; `run_inputs.py` is a newly supplied command-line wrapper, not that historical runner. Its numerical equivalence has not been tested.

The original `GeoChem.dat` database has not been recovered in this package. Its expected SHA-256 is `2cfa5be85bd29bd7556946a0b7f104857ff848d04b18c9f57e9d2508195e72fe`. Do not rename a standard PHREEQC database to imply it is this original file.

With the original database and PHREEQC installed:

```bash
python3 chemistry/run_inputs.py --database /path/to/GeoChem.dat --stem pH_8.5__CaCl2
```

Omit `--stem` to execute all 128 inputs. Outputs are created under `chemistry/generated` and are not distributed in the repository. For an explicitly alternative calculation with the upstream database:

```bash
python3 chemistry/run_inputs.py --database software/phreeqc3/database/phreeqc.dat --allow-alternative-database --stem pH_8.5__CaCl2
```

This second command does not establish exact reproduction of historical results. The wrapper refuses an unmatched database unless the alternative is explicitly acknowledged. Review convergence and database compatibility before interpreting results.

## Mapping and scope

The manuscript uses `f = clip(TBP/0.65, 0, 1)` and `cos(theta) = (1-f) cos(45 degrees) + f cos(135 degrees)`. TBP coefficients 0.28 and 0.50 are model inputs already encoded in the decks. The chemistry is a reduced effective representation, not a calibrated complete asphaltene model. Aqueous chemistry, scalar conditioning and displacement are sequential; these decks do not implement reactive coupling inside interFoam. They do not regenerate a spatial conditioning field without the missing conditioning transport setup. The two supplied displacement cases already contain their prescribed wall-angle inputs.
