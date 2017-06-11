#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_char_set_access.py
----------------------------------

Tests for character set access in the `xn_twist` module.
"""

import os

import pytest


@pytest.fixture
def character_sets():
    """Return the character sets as a pytest fixture."""
    char_sets = [
        {
            'name': "cyrillic_complete",
            'path': "complete/cyrillic_complete.json",
        },
        {
            'name': "cyrillic_advanced",
            'path': "advanced/cyrillic_advanced.json",
        },
        {
            'name': "cyrillic_simple",
            'path': "simplified/cyrillic_simplified.json",
        },
        {
            'name': "greek_complete",
            'path': "complete/greek_complete.json",
        },
        {
            'name': "greek_advanced",
            'path': "advanced/greek_advanced.json",
        },
        {
            'name': "greek_simple",
            'path': "simplified/greek_simplified.json",
        },
        {
            'name': "latin_complete",
            'path': "complete/latin_complete.json",
        },
        {
            'name': "latin_advanced",
            'path': "advanced/latin_advanced.json",
        },
        {
            'name': "latin_simple",
            'path': "simplified/latin_simplified.json",
        },
    ]

    return char_sets


def test_char_set_access(character_sets):
    """Ensure that all of the character sets can be read."""
    for charset in character_sets:
        charset_path = os.path.join(os.getcwd(), "data/", charset['path'])
        with open(charset_path):
            pass
