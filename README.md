# UC Module Python Package

## How To Install

clone repo.
```
cd UC-module
pip install .
```

## How to Use


_*uc.module.UC(measurment=str, dark=str, reference=str, header=boolian)*_ <br>
 - measurment : file path to measurment file. <br>


```
from uc.module import UC

spectrum = UC(measurment='your-measurment-file.txt', dark='your-dark.txt (optional)', reference='your-reference-file.txt', header=False)

spectrum.absorbance()
```
