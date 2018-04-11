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
    parser.add_argument('--sample', type=str, help='Sample file for WCS', required=True)
    parser.add_argument('--path', type=str, help='Path to the directory where the output will be stored', required=True)
    parser.add_argument('--threshold', type=float, help='Counts cutoff in order to trim the image', required=False, default=0)
    parser.add_argument('--clean', type=bool, help='Do you want the image cleaned up?', required=False, default=True)
    parser.add_argument('--radius', type=int, help='Largest radius of the main structure', required=False, default=1000)
    args = parser.parse_args()

    make_slices(args.path, args.input, args.sample, args.min, args.max, args.clean, args.threshold, args.radius)
