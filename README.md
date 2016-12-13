# Internationalized Domain-Squat Finder

Find [internationalized domains](https://en.wikipedia.org/wiki/Internationalized_domain_name "Internationalized Domains") that could be used to spoof a given domain.

**Please note:**

This project is currently under development.

## Usage

```
usage: intl_domain_squat_finder.py [-h] [-cca] [-ccb] [-cs] [-lc] [-ls] [-gc]
                                   [-gs]
                                   domain

Find internationalized domain-squats.

positional arguments:
  domain                Domain name from which to search

optional arguments:
  -h, --help            show this help message and exit
  -cca, --cyrillic_complete_advanced
                        Use complete, advanced Cyrillic character set
  -ccb, --cyrillic_complete_basic
                        Use complete, basic Cyrillic character set
  -cs, --cyrillic_simplified
                        Use simplified Cyrillic character set
  -lc, --latin_complete
                        Use complete Latin character set
  -ls, --latin_simplified
                        Use simplified Latin character set
  -gc, --greek_complete
                        Use complete Greek character set
  -gs, --greek_simplified
                        Use simplified Greek character set
```

## Test Run

To test the internationalized domain-squat finder, clone it, navigate to the ID-SF/ directory and run the following:

`python3 intl_domain_squat_finder.py paypal.com -cs`

## Data, Data, every where...

The datasets in this repository are sample datasets.  I have much more extensive datasets that I do not wish to publish publicly (for fear they will be used maliciously).  In the near future, I will include some contact information where any interested parties can request the complete datasets.
