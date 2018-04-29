#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""XN Twist.

Usage:
    xntwist <domain> [--limit=LIMIT] [--dns] [--output=OUTPUT] [--simple]
    xntwist (-h | --help)
    xntwist --version

Options:
    -h --help     Show this screen.
    --version     Show version.
    -l=LIMIT --limit=LIMIT    Limit the number of characters used as spoofs [default: 5].
    -d --dns  Query DNS for each domain.
    -o=OUTPUT --output=OUTPUT  Specify an output file.
    -s --simple Return only possible squats with one character changed [default: False].
"""

from docopt import docopt

from .__init__ import __version__ as VERSION
from .xn_twist import XNTwist


def main(args=None):
    """Console script for xntwist"""
    arguments = docopt(__doc__, version=VERSION)
    # instantiate XNTwist instance
    xn = XNTwist(query_dns=arguments['--dns'], output=arguments['--output'])

    # twist the given domain
    xn.twist(arguments['<domain>'], limit=arguments['--limit'], simple=arguments['--simple'])


if __name__ == "__main__":
    main()
