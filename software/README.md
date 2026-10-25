# Upstream PHREEQC source

`phreeqc3-b0b3be7.tar.gz` is an unmodified `git archive` snapshot of the USGS upstream repository https://github.com/usgs-coupled-subtrees/phreeqc3 at commit `b0b3be767158ccc3322d2c816625cf470045e67e`, retrieved on 25 October 2026. The authoritative software page is https://www.usgs.gov/software/phreeqc-version-3. The archive includes upstream source, databases, examples, documentation and notices, not calculated results from this study. Its checksum is in `UPSTREAM_SHA256.txt`.

This newly retrieved snapshot is not the historical IPhreeqc/PhreeqcRM library used for the manuscript. Standard databases are not asserted to equal the missing historical GeoChem.dat. Historical hashes are in `../chemistry/historical_run_record.json`.

## Build example

On Linux with a C++ compiler and CMake:

```bash
tar -xzf software/phreeqc3-b0b3be7.tar.gz -C software
cmake -S software/phreeqc3 -B software/build -DCMAKE_BUILD_TYPE=Release
cmake --build software/build --parallel 4
python3 chemistry/run_inputs.py --phreeqc software/build/phreeqc --database /path/to/GeoChem.dat --stem pH_8.5__CaCl2
```

Adjust the executable path for a multi-configuration generator or an installed USGS distribution. `doc/NOTICE.TXT` inside the archive retains upstream usage terms. Source compilation and numerical results have not been tested during packaging. An official installed PHREEQC version 3 can also be used; record its version and database identity for new results.
