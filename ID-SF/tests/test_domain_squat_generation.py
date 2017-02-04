# -*- coding: utf-8 -*-
"""Domain Squat tests."""

import argparse
import unittest

import intl_domain_squat_finder as idsf


DEFAULT_ARGS = argparse.Namespace(cyrillic_advanced=False,
                                  cyrillic_complete=True,
                                  cyrillic_simplified=False,
                                  dns=False, domain='test.com',
                                  greek_advanced=False,
                                  greek_complete=False,
                                  greek_simplified=False,
                                  latin_advanced=False,
                                  latin_complete=False,
                                  latin_simplified=False)

DEFAULT_EMPTY_ARGS = argparse.Namespace(cyrillic_advanced=False,
                                        cyrillic_complete=False,
                                        cyrillic_simplified=False,
                                        dns=False, domain='test.com',
                                        greek_advanced=False,
                                        greek_complete=False,
                                        greek_simplified=False,
                                        latin_advanced=False,
                                        latin_complete=False,
                                        latin_simplified=False)


class TestDSGeneration(unittest.TestCase):
    """."""

    def test_domain_only(self):
        """Test get_spoofable_chars."""
        spoofable_chars = idsf.get_spoofable_charset(DEFAULT_EMPTY_ARGS)
        self.assertEqual(len(spoofable_chars), 0)

    def test_domain_squat_generation(self):
        """Test domain squat creation."""
        count = 0
        spoofable_chars = idsf.get_spoofable_charset(DEFAULT_ARGS)
        self.assertEqual(len(spoofable_chars), 28)
        domain_name, tld = idsf.get_domain_details(DEFAULT_ARGS.domain)
        self.assertEqual(domain_name, "test")
        self.assertEqual(tld, "com")
        spoofable_indices = list()

        # find the index of each 'spoofable' character in the domain
        for char in domain_name:
            if char in spoofable_chars:
                spoofable_indices.append(count)

            count += 1

        combinations = list(idsf.get_combinations(spoofable_indices))
        self.assertEqual(len(combinations), 15)

        domain_squats = idsf.get_possible_domain_squats(domain_name,
                                                        combinations,
                                                        spoofable_chars)
        self.assertEqual(len(domain_squats), 191)
