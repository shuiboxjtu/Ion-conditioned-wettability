#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")" && pwd)
case_name=${1:-Ca2e-5_M15_CaCl2_uniform}
case "$case_name" in
  Ca2e-5_M15_CaCl2_uniform|Ca2e-5_M15_CaCl2_shuffled) ;;
  *) echo 'Choose Ca2e-5_M15_CaCl2_uniform or Ca2e-5_M15_CaCl2_shuffled' >&2; exit 2 ;;
esac
command -v interFoam >/dev/null || { echo 'Source the OpenFOAM v2306 environment first.' >&2; exit 2; }
command -v checkMesh >/dev/null
library_found=false
for directory in "${FOAM_USER_LIBBIN:-}" "${FOAM_LIBBIN:-}"; do
  if [[ -n "$directory" && -f "$directory/libfieldAlphaContactAngle.so" ]]; then library_found=true; fi
done
if [[ "$library_found" != true ]]; then
  echo 'Required libfieldAlphaContactAngle.so is not supplied. Install the compatible original boundary-condition library; do not substitute a uniform-angle wall for the shuffled case.' >&2
  exit 2
fi
cd "$root/$case_name"
if [[ -e log.interFoam || -d postProcessing ]]; then
  echo 'Run in a fresh working copy; existing results will not be overwritten.' >&2
  exit 2
fi
checkMesh > log.checkMesh 2>&1
interFoam > log.interFoam 2>&1
