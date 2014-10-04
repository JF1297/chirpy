#!/usr/bin/env python
# chirp
# Command-line interface for Chirpy
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Sep 26 17:28:14 2014 -0400
#
# For license information, see LICENSE.txt
#
# ID: chirp.py [] benjamin@bengfort.com $

"""
Command-line interface for Chirpy
"""

##########################################################################
## Imports
##########################################################################

import os
import sys
import argparse

## Helper for import
DIRNAME = os.path.dirname(__file__)
PROJECT = os.path.join(DIRNAME, "..")
PATH    = os.path.abspath(PROJECT)

sys.path.append(os.path.abspath(PROJECT))

from chirpy.twitter import TwitterClient

def main(*args):

    parser = argparse.ArgumentParser(description="Command line client for Chirpy",
            version="0.1", epilog="No bugs please!")
    parser.add_argument('query', type=str, nargs="+", help="search term to ingest")

    args   = parser.parse_args()
    client = TwitterClient()
    tweets = client.ingest(" ".join(args.query))
    print "fetched %i tweets" % tweets

if __name__ == '__main__':
    main(*sys.argv[1:])
