# EPICS RPM Spec
RPM Spec files for packaging EPICS components as RPM packages.

Spec file design is based on Michael Davidsaver's original spec file in the EPICS base source tree [https://github.com/mdavidsaver/epics-base/blob/spec/epics-base.spec]

The structure of the spec files and the RPM packages is as following:
1. The spec files create a directory structure under `/opt` as follows  
```
/opt/epics
          /base
          /extensions
          /support
```
  
Where drivers are installed under `/support` and extensions like `edm` and `medm` (Also have been packaged) are installed under `/extensions`.

2. Packages names are simple: `epics-base`, `asyn`, `area-detector-core`, etc.
3. The spec files package everything from the output of `make` command that resides in the `FINAL_LOCATION` variable plus extra folders that might not be packaged like `op`.
4. The directory structure can be changed by changing the `epics_prefix` in any spec file.
5. libraries and executables are installed to `/usr/bin` and `/usr/lib` and symbolic links are installed under the prefix mentioned earlier.
