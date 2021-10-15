import pandas as pd
import numpy as np
import os
from uc.module import UC


def batch_process(dark=None, reference=None, measurments=None, output=None,
                  header=False, spec_type='A'):

    if isinstance(output, str):
        if not '.csv' in output:
            raise f"\"{output}\" is not a valid file name. Should end with \".csv\"." 

    if isinstance(spec_type, str):
        if not spec_type.lower() in ['a', 'r']:
            raise ValueError(f"{spec_type} not valid. Should be one of ['A/a', 'B/b']")
    else:
        raise TypeError(f"spec_type is type {type(spec_type)} but must be a string.")


    wanted_files = [os.path.join(measurments, f) for f in os.listdir(measurments) if '.txt' in f]  # Getting only text_files.
    if not len(wanted_files) > 0:
        raise f"No files found in {measurments}!"

    df_tot = pd.DataFrame() # Empty dataframe
    for i, file in enumerate(wanted_files):  # creating a UC spectrum object for each measurment file in the folder.
        spec = UC(dark=dark, reference=reference, measurment=file, header=header)
        if spec_type.lower() == 'a': # Checks if we want absorbance or transmittance.
            processed_spectrum = spec.absorbance().set_index('wavenumber')
            column_headings = [f"abs_{i}" for i in range(len(wanted_files))] # Generate new column heading for each measurmet.
        elif spec_type.lower() == 'r':
            processed_spectrum = spec.reflectance().set_index('wavenumber')
            column_headings = [f"refl_{i}" for i in range(len(wanted_files))]

        if i == 0:  
            df_tot = processed_spectrum
        else:
            df_tot = pd.concat([df_tot, processed_spectrum], axis=1)

    df_tot.columns = column_headings
    df_tot = df_tot.loc[(4000 >= df_tot.index)]  # Selecting spectral data between 0-4000 cm-1

    if isinstance(output, str):
        df_tot.to_csv(output, decimal=',', sep=';')
    
    return df_tot
    