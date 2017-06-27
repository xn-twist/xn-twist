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
def args():
    """Return the character sets as a pytest fixture."""
    default_args = argparse.Namespace(dns=False, domain='waffle.com')

    return default_args


def test_domain_squat_generation(args):
    """Test the domain squat creation process."""
    spoofable_chars = xn_twist.get_spoofable_charset()
    assert len(spoofable_chars.keys()) == 1

    domain_name, domain_suffix = xn_twist.get_domain_details(args.domain)
    assert domain_name == "waffle"
    assert domain_suffix == "com"

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
