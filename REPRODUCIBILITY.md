# Reproducibility scope and reviewer request

This is an input-only basic-case package. It supplies two control-case configurations and chemical input decks, with instructions and upstream software provenance. It deliberately does not publish calculated simulation data. It does not claim that every principal calculation and manuscript figure can be reproduced from the present repository alone.

| Reviewer request | Supplied here | Remaining limitation |
| --- | --- | --- |
| Geometry and mesh information | Full meshes, patch definitions and time-zero fields for two displacement controls; geometry provenance in cases/README.md | Original CT slices, historical segmentation procedure and reconstruction scripts are not supplied |
| Chemical inputs and parameters | 128 PHREEQC decks, scenario metadata, historical software hashes, pinned upstream source snapshot and CLI wrapper | Historical GeoChem.dat and original IPhreeqc runner are not recovered; the upstream snapshot is not the historical environment |
| Fluid source and setup | Existing IonConWettabilityFoam source; interFoam case dictionaries and properties | fieldAlphaContactAngle custom library source is missing; existing fluid source does not supply it |
| Conditioning and spatial wall assignment | Supplied uniform and shuffled angle lists in initial fields; TBP and angle mapping documented | Original scalar-transport configuration, original spatial field and its complete generation pipeline are not supplied |
| Postprocessing | A script exporting newly generated water-saturation records | This is not the complete manuscript plotting pipeline; pressure, interface, topology, convergence and figure data are not distributed |
| Execution instructions | Case runner, chemistry runner and PHREEQC build instructions | Numerical execution has not been verified in OpenFOAM/PHREEQC as part of packaging |
| Version and persistent identifier | Git commit identifies this package; upstream PHREEQC commit and archive SHA-256 are recorded | No DOI or archived release is claimed; a persistent archived identifier would require a separate deposit |

## Guidance for the response letter

The current response letter should not state that all principal calculations and figures, or the custom boundary-condition implementation, have already been deposited. A description consistent with this package is:

> We have deposited two basic displacement-control case configurations, including their meshes, initial fields, prescribed wall-angle lists and numerical dictionaries, together with the retained PHREEQC inputs, upstream software provenance and execution instructions. Calculated result fields and figure datasets are not included. The repository explicitly identifies the unavailable historical chemistry database, custom contact-angle implementation and conditioning/figure-generation components. The present deposit therefore documents the supplied configurations and parameters but does not yet constitute a complete reproduction package for every principal calculation and figure.

The reviewer's request for full figure/calculation reproducibility remains only partially addressed under an input-only deposit with these missing dependencies. State that scope accurately in the manuscript and reply rather than treating a repository URL as evidence of completeness.
