#!/usr/bin/env python
import argparse
import re

from FGES_BinnedAnalysis import FGES_BinnedAnalysis

if __name__ == "__main__":

    #Collect input
    parser = argparse.ArgumentParser(description="Extract analysis results")
    parser.add_argument('--prefix', type=str, help='Prefix for file names', required=True)
    parser.add_argument('--ANALYSISDIR', type=str, help='Path to directory for the analysis', required=True)
    parser.add_argument('--numsources', type=int, help='Number of sources', required=True)
    parser.add_argument('--xmlsources', type=str, help='Names of sources; enter names separated by commas', required=True)
    parser.add_argument('--spectrum', type=bool, help='Create SED (butterfly plot)?', required=False, default=False)
    parser.add_argument('--spectrumpoints', type=bool, help='Create SED (with points)?', required=False, default=False)
    parser.add_argument('--spectrumpointsUL', type=bool, help='Create SED (with points and upper limits)?', required=False, default=False)
    parser.add_argument('--spectrum_mev_or_erg', type=str, help='MeV or erg on y-axis of SED?', required=False, default='erg')
    parser.add_argument('--spectrum_mev_or_tev', type=str, help='MeV or TeV on x-axis of SED?', required=False, default='tev')
    parser.add_argument('--configfile', type=str, help='Name of config file (not including .yaml)', required=True)

    args = parser.parse_args()

    # Make the sources_elements input into a list from a string
    trimmed = re.sub('[\s+]', '', args.xmlsources)
    xmlsources = trimmed.split(',')

    FGES_BinnedAnalysis(args.prefix,args.ANALYSISDIR,args.numsources,xmlsources,args.spectrum,args.spectrumpoints,
                        args.spectrumpointsUL,args.spectrum_mev_or_erg,args.spectrum_mev_or_tev,args.configfile + '.yaml')