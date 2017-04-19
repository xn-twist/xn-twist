#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_domain_squat_generation.py
----------------------------------

Tests domain squat generation in the `xn_twist` module.
"""

import argparse

import pytest

from xn_twist import xn_twist


@pytest.fixture
def default_args():
    """Return the character sets as a pytest fixture."""
    default_args = argparse.Namespace(cyrillic_advanced=False,
                                      cyrillic_complete=True,
                                      cyrillic_simplified=False,
                                      dns=False, domain='waffle.com',
                                      greek_advanced=False,
                                      greek_complete=False,
                                      greek_simplified=False,
                                      latin_advanced=False,
                                      latin_complete=False,
                                      latin_simplified=False)

    return default_args


@pytest.fixture
def default_empty_args():
    """Return the character sets as a pytest fixture."""
    default_empty_args = argparse.Namespace(cyrillic_advanced=False,
                                            cyrillic_complete=False,
                                            cyrillic_simplified=False,
                                            dns=False, domain='waffle.com',
                                            greek_advanced=False,
                                            greek_complete=False,
                                            greek_simplified=False,
                                            latin_advanced=False,
                                            latin_complete=False,
                                            latin_simplified=False)

    return default_empty_args


def test_domain_only(default_empty_args):
    """Test `get_spoofable_chars` function."""
    spoofable_chars = xn_twist.get_spoofable_charset(default_empty_args)[0]
    assert len(spoofable_chars.keys()) == 0


def test_domain_squat_generation(default_args):
    """Test the domain squat creation process."""
    spoofable_chars = xn_twist.get_spoofable_charset(default_args)[0]
    assert len(spoofable_chars.keys()) == 1

    domain_name, tld = xn_twist.get_domain_details(default_args.domain)
    assert domain_name == "waffle"
    assert tld == "com"

    count = 0
    spoofable_indices = list()
    # find the index of each 'spoofable' character in the domain
    for char in domain_name:
        if char in spoofable_chars:
            spoofable_indices.append(count)

        count += 1

    combinations = list(xn_twist.get_combinations(spoofable_indices))
    assert len(combinations) == 1

    domain_squats = xn_twist.get_possible_domain_squats(domain_name,
                                                        combinations,
                                                        spoofable_chars)
    assert len(domain_squats) == 5
