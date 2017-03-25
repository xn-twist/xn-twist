# -*- coding: utf-8 -*-
"""Character set tests."""

import argparse
import os
import unittest

CHARSET_STATS = [
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


class TestCharSetAccess(unittest.TestCase):
    """Check availability of character sets."""

    @staticmethod
    def test_read_charsets():
        """Ensure that all of the character sets can be read."""
        for charset in CHARSET_STATS:
            charset_path = os.path.join(os.getcwd(), "data/", charset['path'])
            with open(charset_path) as f:
                pass
