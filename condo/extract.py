#!/usr/bin/env python
import argparse
import os
import re

from condo.extract_results import extract_results

if __name__ == "__main__":

    #Collect input
    parser = argparse.ArgumentParser(description="Extract analysis results")
    parser.add_argument('--npy_file', type=str, help='NPY file from analysis', required=True)
    parser.add_argument('--sources_elements', type=str, help='Source elements to be printed; enter in form [,]', required=True)

    args = parser.parse_args()

    # Make the sources_elements input into a list from a string
    trimmed = re.sub('[\s+]', '', args.sources_elements)
    sources_elements = trimmed.split(',')

    extract_results(args.npy_file,sources_elements)