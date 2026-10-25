# Ion-conditioned wettability

Study materials for ion-conditioned wettability fields and pore-scale oil displacement in a reduced calcite-acidic-oil model. Earlier manuscript title: Ion-specific asphaltene-mediated wettability and pore-scale oil displacement.

## Contents

| Directory | Contents |
| --- | --- |
| IonConWettabilityFoam/ | Previously supplied fluid source, unchanged |
| cases/ | Uniform-angle and shuffled-angle CaCl2 controls, including initial fields, meshes and numerical dictionaries |
| chemistry/ | 128 PHREEQC inputs, scenario metadata, historical hashes and a new command-line wrapper |
| software/ | Pinned USGS PHREEQC source archive, provenance and build instructions |

Read [case instructions](cases/README.md), [chemistry instructions](chemistry/README.md), and [PHREEQC source instructions](software/README.md) before execution. [REPRODUCIBILITY.md](REPRODUCIBILITY.md) maps the reviewer requests to the supplied materials and missing components. INPUT_MANIFEST.csv records SHA-256 checksums of case and chemistry files.

## Calculation sequence and dependencies

The study uses sequential brine conditioning, surface equilibrium, TBP-to-contact-angle mapping and frozen-wettability VOF displacement. PHREEQC is not coupled inside each interFoam time step. The two supplied cases already include their prescribed wall-angle lists.

Displacement dictionaries use interFoam/OpenFOAM v2306 and require libfieldAlphaContactAngle.so. Its original implementation is missing from this deposit and from the previously uploaded fluid source; install a compatible original library before running. The top-level Make/files in IonConWettabilityFoam still targets $(FOAM_APPBIN)/interFoam and its include configuration references ../VoF. The directory name does not rename the executable or supply all upstream dependencies.

The original chemistry database GeoChem.dat is absent. Standard databases in the newly downloaded upstream source are not silently substituted for it. See chemistry/README.md for explicit alternative-database calculations and their limitations.

## Exclusions and verification

No study simulation-result fields, nonzero time directories, processor output, logs, postProcessing data, manuscript figures or result tables are distributed. Meshes and initial wall-angle lists are retained as required inputs. Only the two CaCl2 controls are included; the separate bubble benchmark is excluded.

This is a basic input package, not a complete reproduction archive for every manuscript calculation and figure. Numerical build/run validation was not performed during packaging. No archived-release DOI is claimed. Existing OpenFOAM copyright and GPL notices are retained; upstream PHREEQC notices are inside its unmodified archive.