# UpconversionTools Python Package

* [General Theory](#general-theory)
* [Installation](#installation)
* [Usage](#usage)
* [CLI](#cli)
* [Documentation](#documentation)

## General Theory

When a spectrum is measured using the upconversion module you are measuring light
in the NIR-Vis region instead of the mid-IR regions. This is the results of the non-linear
optical process taking place in the upconversion module, which effectivly transposes the
infrared light up to NIR-Vis. This way we build small and compact systems and use regular
silicon-based spectrometers such as the OceanOptics/Insight products.

Since our measured light is in NIR-Vis we need to transpose the NIR-Vis spectrum to
the corresponding IR spectrum (in reciprocal centimiters). This is done using a simple transformation of the 
wavelength of the measured light like so:
 
<img src="https://latex.codecogs.com/svg.image?\hat{\nu}&space;\,&space;[cm^{-1}]&space;=&space;\left(&space;\frac{1}{\lambda_{up.}}&space;-&space;\frac{1}{1065}&space;&space;\right)10^{7}" title="\hat{\nu} \, [cm^{-1}] = \left( \frac{1}{\lambda_{up.}} - \frac{1}{1065} \right)10^{7}" />

## Installation

Clone the UpconversionTools repository.
```
cd UpconversionTools
pip install .
```

# Usage

## Working with single spectrum.

```
from uc.module import UC

spectrum = UC(measurment='your-measurment-file.txt', dark='your-dark.txt (optional)', reference='your-reference-file.txt', header=False)

spectrum.absorbance()
```


## Batch Processing files:

To batch process a folder with spectra, collected from an In-situ measurment you can use the
batch-module of the UpconversionTools package.

```
from uc.batch import batch_process

batch_process(measurments=<path-to-measurment-files-folder>, dark=<you-dark-spectrum (Optional if you already subtracted the dark spectrum
when measuring.>, reference=<your-reference-spectrum>, output=<the-path-and-name-of-results-file>, header=<if-the-files-contain-headers>,
spec_type='A)

```
# CLI

## Using the CLI to batch process files (Command Line Interface)

UpconversionTools also comes with a CLI to be used in the command line or terminal. This
is convenient to quickly process many files.

In the terminal/CMD (Obs. use the Anaconda3-Prompt if Anaconda is installed). Use the -h flag to see how to use the tool.

Ex:
```
ucmod -s <your-folder-with-spectra> -d <your-dark-spectrum (optional)> -r <your-ref-spectrum> -o <name-and-location-of-results-file> --header (if files have headers) -t R (gives reflectance)

```

# Documentation
___
__*uc.module.UC(measurment=str, dark=str, reference=str, header=boolian)*__ <br>
__Parameters__: <br>
__measurment__ <br>

> file path to measurment file. <br>

__dark__ <br>
> file path to dark spectrum. <br>

__reference__ <br>
> file path to reference spectrum. <br>

__header__ <br>
> (True/False) If the datafiles contain header with metadata (if you choose this option in OceanView/SpectraSuite.

__Returns__: <br>
> An instance of the UC module class.
___
__*uc.module.UC.absorbance()*__ <br>
> Converts the spectral data to absorbance [lg(reflectance)].

__Returns__ <br>
> Pandas Dataframe: A pandas dataframe containing your UC corrected IR spectrum in Absorbance.
___
__*uc.module.UC.reflectance()*__ <br>
> Converts the spectral data to absorbance [lg(reflectance)].

__Returns__ <br>
> Pandas Dataframe: A pandas dataframe containing your UC corrected IR spectrum in Absorbance.

___
__*uc.batch.batch_process(measurments, dark, reference, output,
                  header=False, spec_type='A'):*__ <br>
__Parameters__:
__measurment__ <br>
>
> file path to folder containing the spectra. <br>
__dark__ <br>
> file path to dark spectrum. <br>
__reference__ <br>
> file path to reference spectrum. <br>
__output__ <br>
> The path + name to you the output file which will contain your spectra. e.g.
__header__ <br>
> (True/False) If the datafiles contain header with metadata (if you choose this option in OceanView/SpectraSuite.
__spec_type__ <br>
> Desired type of spectrum 'A' : Absorbance, 'R': Reflectance.
