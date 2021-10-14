import pandas as pd
import numpy as np

class UC:
    """[Det her er en UC python classe]

    Returns:
        [type]: [description]
    """

    mixing_laser_wavelength = 1064

    def __init__(self, dark=None, reference=None, measurment=None, header=False):
        
        ## HELPER ATTRIBUTES
        self.header = header

        ## SPECTRAL DATA
        if dark:
            self.dark = self.read_spectrum(dark)
        else:
            self.dark = dark

        if reference:    
            self.reference = self.read_spectrum(reference)
        else:
            self.reference = reference

        if measurment:
            self.measurment = self.read_spectrum(measurment)
        else:
            self.measurment = measurment

        self.processed_spectrum = None
        

    def __str__(self):
        return 'UC_spectrum'
    
    def read_spectrum(self, file):

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

        df = self.measurment.copy()
        df['reflectance'] = self.measurment['intensity']/self.reference['intensity']
        df.drop(columns=['intensity'], inplace=True)
        self.processed_spectrum = df

        return self.processed_spectrum

    def absorbance(self):

        df = self.measurment.copy()
        df['absorbance'] = -1*np.log(self.measurment['intensity']/self.reference['intensity'])
        df.drop(columns=['intensity'], inplace=True)

        self.processed_spectrum = df
        return self.processed_spectrum


