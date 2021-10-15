#!/usr/bin/env python

import pandas as pd
import numpy as np

class UC:
    """This is a python

    Returns:
        [type]: [description]
    """

    mixing_laser_wavelength = 1064  # [nm] wavelength of mixing laser.

    def __init__(self, dark=None, reference=None, measurment=None, header=False):
        
        ## HELPER ATTRIBUTES
        self.header = header

        ## SPECTRAL DATA
        if dark:  # Checks if dark spectrum is given.
            self.dark = self.read_spectrum(dark)
        else:
            self.dark = dark

        if reference:  # Checks if reference spectrum is given.
            self.reference = self.read_spectrum(reference)
        else:
            self.reference = reference

        if measurment:  #  Checks if measurment spectrum is given.
            self.measurment = self.read_spectrum(measurment)
        else:
            self.measurment = measurment

        self.processed_spectrum = None  # Create the processed_spectrum attribute
        

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        
        return 'UC_spectrum'
    
    def read_spectrum(self, file):
        """[summary]

        Args:
            file ([type]): [description]

        Returns:
            [type]: [description]
        """

        if self.header:
            df = pd.read_csv(
                file,
                engine='python',
                skiprows=17,
                skipfooter=1,
                decimal=',',
                sep='\t',
                names=['wavelength', 'intensity']
            )

        else:
            df = pd.read_csv(
                file,
                engine='python',
                decimal=',',
                sep='\t',
                names=['wavelength', 'intensity']
            )

        df['wavenumber'] = df['wavelength'].apply(lambda x: (1/x - 1/self.mixing_laser_wavelength)*1e7)
        df.drop(columns=['wavelength'], inplace=True)

        return df

    def reflectance(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        df = self.measurment.copy()
        df['reflectance'] = self.measurment['intensity']/self.reference['intensity']
        df.drop(columns=['intensity'], inplace=True)
        self.processed_spectrum = df

        return self.processed_spectrum

    def absorbance(self):
        """[summary]

        Returns:
            [type]: [description]
        """

        df = self.measurment.copy()
        df['absorbance'] = -1*np.log(self.measurment['intensity']/self.reference['intensity'])
        df.drop(columns=['intensity'], inplace=True)

        self.processed_spectrum = df
        return self.processed_spectrum


