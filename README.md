# Ion-conditioned-wettability

Ion-specific asphaltene-mediated wettability and pore-scale oil displacement.

## Source code

The `IonConWettabilityFoam/` directory contains the solver source files supplied for this repository, including `Make/files`, `Make/options`, and the `interMixingFoam/` and `overInterDyMFoam/` subdirectories.

The source is preserved as supplied. The top-level build target in `IonConWettabilityFoam/Make/files` is currently `$(FOAM_APPBIN)/interFoam`; the directory name does not rename the executable. Building requires a compatible OpenFOAM installation and the dependencies and include paths specified in the Make configuration, including the relative `../VoF` include path. This repository does not currently include simulation cases or a verified standalone build procedure. Compilation and simulation have not been tested as part of this upload.

Existing OpenFOAM copyright and GNU GPL license notices are retained in the source files.