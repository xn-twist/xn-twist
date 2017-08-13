===============================
XN Twist
===============================

.. image:: https://img.shields.io/pypi/v/xn-twist.svg
        :target: https://pypi.python.org/pypi/xn-twist

.. image:: https://travis-ci.org/xn-twist/xn-twist.svg?branch=master
    :target: https://travis-ci.org/xn-twist/xn-twist

.. image:: https://codecov.io/gh/xn-twist/xn-twist/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/xn-twist/xn-twist

.. image:: https://api.codacy.com/project/badge/Grade/166ee00207f5497da6316e35f4262bc0
     :alt: Codacy Badge
     :target: https://www.codacy.com/app/fhightower/xn-twist

.. image:: https://readthedocs.org/projects/xn-twist/badge/?version=latest
        :target: http://xn-twist.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/xn-twist/xn-twist/shield.svg
     :target: https://pyup.io/repos/github/xn-twist/xn-twist/
     :alt: Updates

*Find Unicode domain squats*

Installation
============

Stable release
--------------

To install XN Twist, run this command in your terminal:

.. code-block:: console

    pip install xn-twist

This is the preferred method to install XN Twist, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/

From sources
------------

The sources for XN Twist can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/xn-twist/xn-twist

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/xn-twist/xn-twist/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

.. _Github repo: https://github.com/xn-twist/xn-twist
.. _tarball: https://github.com/xn-twist/xn-twist/tarball/master

Usage
=====

Via Python
----------

You can use XN-Twist in a script as follows:

.. code-block:: python

    from xn_twist.xn_twist import XNTwist
    xn = XNTwist()
    domain_twist_results = xn.twist("example.com")

Via Command Line
----------------

You can use XN-Twist from the command line as follows:

.. code-block:: shell

    xntwist example.com

The usage for the command line form of XN-Twist is as follows:

.. code-block::

    XN Twist.

    Usage:
        xntwist <domain> [--dns] [--output=OUTPUT]
        xntwist (-h | --help)
        xntwist --version

    Options:
        -h --help     Show this screen.
        --version     Show version.
        -d --dns  Query DNS for each domain.
        -o=OUTPUT --output=OUTPUT  Specify an output file.

Run Tests
=========

After cloning the repo, you can test it using the following commands from the base directory of this repository:

.. code-block:: shell

    make test

Data, Data, Everywhere...
==========================

This project relies on a dataset. More details on how to access the dataset and even how to help us build it coming soon!

Credits
=======

This package was created with Cookiecutter_ and the `fhightower/python-project-template`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fhightower/python-project-template`: https://github.com/fhightower/python-project-template
