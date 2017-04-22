===============================
XN Twist
===============================


.. image:: https://img.shields.io/pypi/v/xn_twist.svg
        :target: https://pypi.python.org/pypi/xn_twist

.. image:: https://img.shields.io/travis/fhightower/xn_twist.svg
        :target: https://travis-ci.org/fhightower/xn_twist

.. image:: https://codecov.io/gh/fhightower/xn_twist/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/fhightower/xn_twist

.. image:: https://readthedocs.org/projects/xn_twist/badge/?version=latest
        :target: https://xn_twist.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/fhightower/xn_twist/shield.svg
     :target: https://pyup.io/repos/github/fhightower/xn_twist/
     :alt: Updates

*Internationalized Domain-Squat Finder*

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

- ``cd xn_twist;``
- ``nosetests tests/``

If you do not have installed, you can also use Python's built-in [unittest](https://docs.python.org/3/library/unittest.html) command:

- ``cd xn_twist;``
- ``python3 -m unittest``

**Note:** Tests will return failures and errors if the character sets are not included. This is expected.

Data, Data, every where...
==========================

The character sets in the ``xn_twist/data`` directory of this repository are sample character sets. I have much more extensive character sets that I do not wish to publish publicly (for fear they will be used maliciously). In the near future, I will include some contact information where any interested parties can request the character sets.

Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

