# Basic displacement cases

The two cases are `Ca2e-5_M15_CaCl2_uniform` and `Ca2e-5_M15_CaCl2_shuffled`. Only `0`, `constant` and `system` are distributed. Numerical meshes and prescribed time-zero wall-angle lists are necessary inputs; they are retained. Nonzero-time fields, processor results, postProcessing, logs, status directories and manuscript figure data are excluded. The separate Su2019 bubble case is not part of this upload.

Both use interFoam/OpenFOAM v2306, Ca = 2e-5, dynamic viscosity ratio M = 15, inlet velocity 0.00100135182496 m/s, and interfacial tension 0.05 N/m. The mesh is planar and extruded through one layer: 120816 cells, front/back empty patches, 58086 solid-wall faces, 52 inlet faces and 464 outlet faces. The source image provenance is DRSRD1, DOI https://doi.org/10.17612/P7D38H; calcite chemistry is assigned to a sandstone-derived geometry. Historical slice identifiers and segmentation thresholds have not been recovered. No original CT collection is redistributed.

The uniform case sets the solid-wall water-side angle to 97.46203254 degrees. The shuffled case supplies a nonuniform angle list aligned to mesh patch order. Do not reorder the mesh faces independently of the angle list. The scalar conditioning calculation and original unshuffled wall field are not supplied here. This pair supports a basic control-case setup, not reconstruction of all twenty manuscript configurations or arbitrary correlation-length realizations.

## Dependencies and run

Both dictionaries load `libfieldAlphaContactAngle.so` and both initial alpha fields use `fieldAlphaContactAngle`. Its original implementation is not present in the recovered source files. The existing `IonConWettabilityFoam` directory does not provide this library. A compatible implementation must be obtained and built in the OpenFOAM v2306 environment before these cases can run. This is a missing dependency, not a built-in boundary condition. No replacement implementation is silently introduced in this release.

In a fresh working copy, after sourcing OpenFOAM v2306 and installing that library:

```bash
bash cases/run_case.sh Ca2e-5_M15_CaCl2_uniform
bash cases/run_case.sh Ca2e-5_M15_CaCl2_shuffled
python3 cases/extract_saturation.py cases/Ca2e-5_M15_CaCl2_uniform > uniform_saturation.csv
```

The meshes are supplied, so blockMesh/setFields are not needed. The dictionaries retain `startFrom latestTime`; a fresh package contains only time 0. Work from fresh copies to avoid unintended restarts. Serial execution is shown to preserve the supplied mesh-to-wall-angle ordering. Parallel mapping of the custom boundary condition has not been verified.

Initial fields, physical properties, schemes, pressure and velocity solver tolerances, PIMPLE settings and adaptive time-step controls are given directly in the dictionaries. The saturation function object records the volume average of alpha.water; the extraction script exports this recorded quantity without clipping or reinterpreting it as gross cumulative production. The supplied end time is approximately 1 injected pore volume using manuscript pore volume 5.4013e-10 m3 and inlet area 3.4324e-8 m2. Pressure-history, interface-length and topology figure pipelines are not included; see `../REPRODUCIBILITY.md`.
