#!/usr/bin/env python
import argparse

from get_sourcemap import get_sourcemap

if __name__ == "__main__":

    #Collect input
    parser = argparse.ArgumentParser(description="Make sourcemap")
    parser.add_argument('--path', type=str, help='Path to directory for analysis', required=True)
    parser.add_argument('--prefix', type=str, help='Prefix for file names (ie. name of source)', required=True)
    parser.add_argument('--suffix', type=str, help='Suffix for file names (ie. energy range)', required=True)
    parser.add_argument('--sources', type=str, help='Source names or other file descriptor', required=True)

    args = parser.parse_args()

    get_sourcemap(args.path,args.prefix,args.suffix,args.sources)