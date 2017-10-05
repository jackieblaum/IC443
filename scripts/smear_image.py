#!/usr/bin/env python
import argparse
import os

from ic443.convolve import convolve

if __name__ == "__main__":

    #Collect input
    parser = argparse.ArgumentParser(description="Slice FITS file")
    parser.add_argument('--fits', type=str, help='Fits image to smear', required=True)
    parser.add_argument('--sigma', type=float, help='Gaussian sigma for convolution', required=True)
    parser.add_argument('--mode', type=str, help='Mode for convolution', required=False, default='nearest')
    parser.add_argument('--outfile', type=str, help='Name of output file (not including .fits)', required=True)

    args = parser.parse_args()

    convolve(args.fits, args.sigma, args.mode, args.outfile)

