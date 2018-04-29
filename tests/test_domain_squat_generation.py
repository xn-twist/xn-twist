#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_domain_squat_generation.py
----------------------------------

Tests domain squat generation in the `xn_twist` module.
"""

from datetime import datetime

import pytest

from xn_twist import XNTwist, __version__


@pytest.fixture
def domain():
    """Provide a domain for the tests."""
    return "abc.com"


def test_return_json_format(domain):
    """Test the domain squat creation process."""
    xn = XNTwist()
    twist_results = xn.twist(domain)

    assert len(twist_results.keys()) == 4
    assert twist_results['datetime'].split("-")[0] == str(datetime.today().year)
    assert twist_results['xn_twist_version'] == __version__
    assert len(twist_results['possible_squats']) == 215


def test_limit(domain):
    """Test the domain squat creation process."""
    xn = XNTwist()
    twist_results = xn.twist(domain, limit=2)

    assert len(twist_results.keys()) == 4
    assert twist_results['datetime'].split("-")[0] == str(datetime.today().year)
    assert twist_results['xn_twist_version'] == __version__
    assert len(twist_results['possible_squats']) == 26


def test_simple(domain):
    """Test the domain squat creation process with the simple mode turned on."""
    xn = XNTwist()
    twist_results = xn.twist(domain, simple=True)

    assert len(twist_results.keys()) == 4
    assert twist_results['datetime'].split("-")[0] == str(datetime.today().year)
    assert twist_results['xn_twist_version'] == __version__
    assert len(twist_results['possible_squats']) == 15
