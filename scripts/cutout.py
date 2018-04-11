#!/usr/bin/env python
import argparse
import os

from ic443.ds9reg_cutout import ds9reg_cutout

if __name__ == "__main__":

    #Collect input
    parser = argparse.ArgumentParser(description="Make DS9 region cutout from FITS file")
    parser.add_argument('--infile', type=str, help='Input file', required=True)
    parser.add_argument('--regname', type=str, help='Name of DS9 region (not including .reg)', required=True)
    parser.add_argument('--binsize', type=float, help='Size of bins', required=False, default='0.025')
    parser.add_argument('--outfile', type=str, help='Name of output file (not including .fits)', required=True)
    parser.add_argument('--path', type=str, help='Name of path to output', required=True)

    args = parser.parse_args()

    ds9reg_cutout(args.path, args.infile + '.fits', args.outfile, args.regname + '.reg', args.binsize)