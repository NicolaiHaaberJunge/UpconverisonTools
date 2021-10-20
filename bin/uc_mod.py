#!/usr/bin/env python

import os
import argparse as ap
import pandas as pd
from uc.batch import batch_process



def main():
    
    parser = ap.ArgumentParser(prog='ucmod', description='Batch tool for converting UC spectra to IR spectra.')
    
    # String valued arguments
    parser.add_argument('-s', '--spectra', type=str, help="Path to folder containing UC spectra.")
    parser.add_argument('-d', '--dark', type=str, help="Path to dark spectrum.")
    parser.add_argument('-r', '--reference', type=str, help="Path to reference spectrum.")
    parser.add_argument('-o', '--out', type=str, help="output file")

    # Bool or list values arguments
    parser.add_argument('--header', action="store_true", help='Spectrum files contain header metadata.')
    parser.add_argument('-t', '--type',
                         type=str,
                         choices=['A', 'a', 'R', 'r'],
                         default='A',
                         help='Desired spectrum type e.g lg(Reflectance) [A, a] or Reflectance [R, r].')

    args = parser.parse_args()  # Parsing arguments to args object.

    ## Batch process
    batch_process(
        dark=args.dark,
        reference=args.reference,
        measurments=args.spectra,
        output=args.out,
        header=args.header,
        spec_type=args.type)

    ## Print confirmation

    list_of_files = os.listdir(args.spectra)
    type_of_spectra = {
        'a' : 'Log(R)',
        'r' : 'Reflectance'
    }

    print_stmt = f'Processed {len(list_of_files)} UC spectra to IR-{type_of_spectra[args.type.lower()]} \n' \
                 f'and saved to {args.output}.'
    print(print_stmt)

    return



if __name__ == '__main__':
    main()
