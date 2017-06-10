===============================
XN Twist
===============================

.. image:: https://img.shields.io/pypi/v/xn_twist.svg
        :target: https://pypi.python.org/pypi/xn_twist

.. image:: https://travis-ci.org/xn-twist/xn-twist.svg?branch=master
    :target: https://travis-ci.org/xn-twist/xn-twist

.. image:: https://codecov.io/gh/xn-twist/xn-twist/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/xn-twist/xn-twist

.. image:: https://readthedocs.org/projects/xn-twist/badge/?version=latest
        :target: http://xn-twist.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/xn-twist/xn-twist/shield.svg
     :target: https://pyup.io/repos/github/xn-twist/xn-twist/
     :alt: Updates

.. image:: https://www.quantifiedcode.com/api/v1/project/7024cddb727449fb8ae21ebd29fdc459/badge.svg
        :target: https://www.quantifiedcode.com/app/project/7024cddb727449fb8ae21ebd29fdc459
        :alt: Code issues

*Unicode Domain-Squat Finder*

Installation
============

*More details coming soon...*

Usage
=====

.. code-block:: shell

    usage: xn_twist.py [-h] [-cc] [-ca] [-cs] [-lc] [-la] [-ls] [-gc] [-ga] [-gs] [-d] [-o [OUTPUT]] domain

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
      -d, --dns             Query DNS for each domain
      -o [OUTPUT], --output [OUTPUT]
                            Path to file to which results will be written

Run Tests
=========

After cloning the repo, you can test it using the following commands from the base directory of this repository:

- ``cd xn-twist;``
- ``pytest``

Data, Data, Everywhere...
==========================

*More details coming very soon*

Credits
=======

This package was created with Cookiecutter_ and the `fhightower/python-project-template`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fhightower/python-project-template`: https://github.com/fhightower/python-project-template
