# XN-Twist
*Internationalized Domain-Squat Finder*

[![Build Status](https://travis-ci.org/fhightower/xn-twist.svg?branch=master)](https://travis-ci.org/fhightower/xn-twist)
[![codecov](https://codecov.io/gh/fhightower/xn-twist/branch/master/graph/badge.svg)](https://codecov.io/gh/fhightower/xn-twist)

Find [internationalized domains](https://en.wikipedia.org/wiki/Internationalized_domain_name "Internationalized Domains") that could be used to spoof a given domain.

## Usage

```
usage: intl_domain_squat_finder.py [-h] [-cc] [-ca] [-cs] [-lc] [-la] [-ls]
                                   [-gc] [-ga] [-gs] [-d]
                                  domain

Find internationalized domain-squats.

positional arguments:
 domain               Domain name from which to search

optional arguments:
  -h, --help           show this help message and exit
  -cc, --cyrillic_complete
                       Use complete Cyrillic character set
  -ca, --cyrillic_advanced
                       Use advanced Cyrillic character set
  -cs, --cyrillic_simplified
                       Use simplified Cyrillic character set
  -lc, --latin_complete
                       Use complete Latin character set
  -la, --latin_advanced
                       Use advanced Latin character set
  -ls, --latin_simplified
                       Use simplified Latin character set
  -gc, --greek_complete
                       Use complete Greek character set
  -ga, --greek_advanced
                       Use advanced Greek character set
  -gs, --greek_simplified
                       Use simplified Greek character set
  -d, --dns            Query DNS for each domain
```

## Run Tests

After cloning the repo, you can test it using the following commands from the top directory of this repository:

- `cd idsf;`
- `nosetests tests/`

If you do not have installed, you can also use Python's built-in [unittest](https://docs.python.org/3/library/unittest.html) command:

- `cd idsf;`
- `python3 -m unittest`

**Note:** Tests will return failures and errors if the character sets are not included. This is expected.

## Data, Data, every where...

The character sets in the `data` directory of this repository are sample character sets. I have much more extensive character sets that I do not wish to publish publicly (for fear they will be used maliciously). In the near future, I will include some contact information where any interested parties can request the character sets.
