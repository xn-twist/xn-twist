#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_domain_squat_generation.py
----------------------------------

Tests domain squat generation in the `xn_twist` module.
"""

import argparse
import datetime

import pytest

from xn_twist.xn_twist import XNTwist


@pytest.fixture
def domain():
    """Provide a domain for the tests."""
    return "abc.com"


def test_return_json_format(domain):
    """Test the domain squat creation process."""
    xn = XNTwist()

    twist_results = xn.twist(domain)

    # make sure the json only has one, top-level key
    assert len(twist_results.keys()) == 1

    # make sure the top-level key has today's date in it
    assert str(datetime.datetime.today().year) in list(twist_results.keys())[0]

    # test to make sure that the version number is printed in the output json
    for sub_key in twist_results[list(twist_results.keys())[0]]:
        assert ("version" in sub_key or domain in sub_key)


def test_api_handling():
    """Test the response from the API."""
    # TODO: Add better tests here that use mock to simulate an API (2)
    pass
