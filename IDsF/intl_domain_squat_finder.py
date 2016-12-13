#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# September 2016
# ----------------------------------------------------------------------------
# Copyright (c) 2016 Floyd Hightower
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------
"""Find internationalized domain squats of a given domain."""


import argparse
import itertools
import json
import os
import urllib.parse


def init_parser():
    """Initialize the argument parser."""
    parser = argparse.ArgumentParser(description='Find internationalized ' +
                                                 'domain squats')

    # get domain from which internationalized domains squats will be derived
    parser.add_argument('domain', help='Domain name from which to search.')

    # dataset arguments to create possible internationalized domain squats
    parser.add_argument('-cca', '--cyrillic_complete_advanced',
                        action='store_true',
                        help='Use complete, advanced Cyrillic character set')
    parser.add_argument('-ccb', '--cyrillic_complete_basic',
                        action='store_true',
                        help='Use complete, basic Cyrillic character set')
    parser.add_argument('-cs', '--cyrillic_simplified',
                        action='store_true',
                        help='Use simplified Cyrillic character set')
    parser.add_argument('-lc', '--latin_complete', action='store_true',
                        help='Use complete Latin character set')
    parser.add_argument('-ls', '--latin_simplified', action='store_true',
                        help='Use simplified Latin character set')
    parser.add_argument('-gc', '--greek_complete', action='store_true',
                        help='Use complete Greek character set')
    parser.add_argument('-gs', '--greek_simplified', action='store_true',
                        help='Use simplified Greek character set')

    return parser.parse_args()


def get_spoofable_charset(arguments):
    """Retrieve and return the data from the desired character sets."""
    spoofable_charset = dict()

    base_dataset_path = os.path.join(os.getcwd(), "../data/")
    dataset_paths = {
        'cyrillic_complete_advanced': "complete/cyrillic_advanced.json",
        'cyrillic_complete_basic': "complete/cyrillic_basic.json",
        'cyrillic_simplified': "simplified/cyrillic_simplified.json",
        'latin_complete': "complete/latin_basic.json",
        'latin_simplified': "simplified/latin_simplified.json",
        'greek_complete': "complete/greek_basic.json",
        'greek_simplified': "simplified/greek_simplified.json"
    }

    for arg_name, arg_value in arguments._get_kwargs():
        # if the argument is one that may be specifying a character set...
        if arg_name in dataset_paths:
            # if we want to read this character set...
            if arg_value:
                with open(os.path.join(base_dataset_path,
                                       dataset_paths[arg_name]),
                          'r') as data_file:
                    character_set = json.load(data_file)
                    # iterate through each char and its spoofs from char set
                    for character, spoofs in character_set.items():
                        # if character is already in the spoofable charset...
                        if spoofable_charset.get(character):
                            # append the spoofable chars to the end of the list
                            spoofable_charset[character].extend(spoofs)
                        # if the character is not in the spoofable charset...
                        else:
                            # add character and spoofs to the spoofable charset
                            spoofable_charset[character] = spoofs

    return spoofable_charset


def get_domain_details(domain):
    """Return the domain name and the top level domain (tld)."""
    parsed_domain = urllib.parse.urlparse(domain)

    domain_name = parsed_domain.path.split(".")[0]
    tld = parsed_domain.path.split(".")[1].split("/")[0]

    return domain_name, tld


def get_combinations(index_list):
    """Get all combinations of the domain name's 'spoofable' indices."""
    return (combination
            for combination in itertools.chain.from_iterable(
                itertools.combinations(index_list, i)
                for i in range(1, len(index_list) + 1))
            )


def get_possible_domain_squats(domain_name, combinations, SPOOFABLE_CHARS):
    """Construct all of the possible internationalized domain squats."""
    domains = list()

    for combo in combinations:
        # collect all possible domain squats for this combo.
        temp_combo_domains = list()
        temp_combo_domains.append(domain_name)

        for index in combo:
            # collect domain squats created by changing char. at this index
            temp_index_domains = list()

            # iterate through all domain squats collected so far for this combo
            for domain in temp_combo_domains:
                for spoofed_char in SPOOFABLE_CHARS[domain[index]]:
                    # replace the appropriate, spoofed character
                    new_domain = domain[:index] + spoofed_char

                    # if current index is not the last char. in the domain name
                    if len(domain) > (index + 1):
                        # add the ending of the domain
                        new_domain = new_domain + domain[(index + 1):]

                    # add to list of domains created by changing char at index
                    temp_index_domains.append(new_domain)
            # add to domains created by changing chars. at indices in combo
            temp_combo_domains = temp_index_domains

        # add to list of domain squats
        domains.extend(temp_combo_domains)

    return domains


def display_possible_domain_squats(possible_domain_squats, tld):
    """Display each of the possible, internationalized domain squats."""
    print("{} results found.\n".format(len(possible_domain_squats)))

    for squat in possible_domain_squats:
        print("{}.{}  -".format(squat, tld) +
              "  xn--{}.{}".format(
              str(squat.encode("punycode").decode("utf-8")), tld))


def main():
    """Find the internationalized domain squats for a given domain."""
    # parse the arguments
    args = init_parser()

    SPOOFABLE_CHARS = get_spoofable_charset(args)

    # get the domain from which we should look for domain squats
    domain_name, tld = get_domain_details(args.domain)

    count = 0
    spoofable_indices = list()

    # find the index of each 'spoofable' character in the domain
    for char in domain_name:
        if char in SPOOFABLE_CHARS:
            spoofable_indices.append(count)

        count += 1

    # find all possible combinations of the 'spoofable' indices
    combinations = list(get_combinations(spoofable_indices))

    # create each domain squat
    possible_domain_squats = get_possible_domain_squats(domain_name,
                                                        combinations,
                                                        SPOOFABLE_CHARS)

    # display each possible domain squat
    display_possible_domain_squats(possible_domain_squats, tld)


if __name__ == '__main__':
    main()
