#!/usr/bin/env python
import argparse
import os

from ic443.make_slices import make_slices

if __name__ == "__main__":

    #Collect input
    parser = argparse.ArgumentParser(description="Slice FITS file")
    parser.add_argument('--min', type=int, help='Minimum slice number', required=True)
    parser.add_argument('--max', type=int, help='Maximum slice number', required=True)
    parser.add_argument('--input', type=str, help='Input FITS file', required=True)

    args = parser.parse_args()

    make_slices(args.input, args.min, args.max)
