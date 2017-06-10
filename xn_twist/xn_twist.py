#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# This project is licensed under an MIT License.
"""Find internationalized domain-squats of a given domain."""


import argparse
import datetime
import itertools
import json
import os
import time
import urllib.parse

import dns.resolver


CURRENT_DATETIME = str(datetime.datetime.today())
CHAR_SET_VERSION = 0.1
FUZZER_VERSION = 0.9


def init_parser():
    """Initialize the argument parser."""
    parser = argparse.ArgumentParser(description='Find internationalized ' +
                                                 'domain-squats.')

    # get domain from which internationalized domains squats will be derived
    parser.add_argument('domain', help='Domain name from which to search')

    # dataset arguments to create possible internationalized domain squats
    parser.add_argument('-cc', '--cyrillic_complete',
                        action='store_true',
                        help='Use complete Cyrillic character set')
    parser.add_argument('-ca', '--cyrillic_advanced',
                        action='store_true',
                        help='Use advanced Cyrillic character set')
    parser.add_argument('-cs', '--cyrillic_simplified',
                        action='store_true',
                        help='Use simplified Cyrillic character set')
    parser.add_argument('-lc', '--latin_complete', action='store_true',
                        help='Use complete Latin character set')
    parser.add_argument('-la', '--latin_advanced', action='store_true',
                        help='Use advanced Latin character set')
    parser.add_argument('-ls', '--latin_simplified', action='store_true',
                        help='Use simplified Latin character set')
    parser.add_argument('-gc', '--greek_complete', action='store_true',
                        help='Use complete Greek character set')
    parser.add_argument('-ga', '--greek_advanced', action='store_true',
                        help='Use advanced Greek character set')
    parser.add_argument('-gs', '--greek_simplified', action='store_true',
                        help='Use simplified Greek character set')
    parser.add_argument('-d', '--dns', action='store_true',
                        help='Query DNS for each domain')
    parser.add_argument('-o', '--output', nargs='?',
                        help='Path to file to which results will be written')

    return parser.parse_args()


def get_spoofable_charset(arguments):
    """Retrieve and return the data from the desired character sets."""
    spoofable_charset = dict()
    charsets_used = list()

    base_dataset_path = os.path.join(os.getcwd(), "data/")
    dataset_paths = {
        'cyrillic_complete': "complete/cyrillic_complete.json",
        'cyrillic_advanced': "advanced/cyrillic_advanced.json",
        'cyrillic_simplified': "simplified/cyrillic_simplified.json",
        'latin_complete': "complete/latin_complete.json",
        'latin_advanced': "advanced/latin_advanced.json",
        'latin_simplified': "simplified/latin_simplified.json",
        'greek_complete': "complete/greek_complete.json",
        'greek_advanced': "advanced/greek_advanced.json",
        'greek_simplified': "simplified/greek_simplified.json"
    }

    for arg_name, arg_value in arguments._get_kwargs():
        # if the argument specifies a dataset that we want to pull in...
        if arg_name in dataset_paths and arg_value:
            charsets_used.append(arg_name)
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

    return spoofable_charset, charsets_used


def get_domain_details(domain):
    """Return the domain name and the top level domain (tld)."""
    parsed_domain = urllib.parse.urlparse(domain)

    domain_name = parsed_domain.path.split(".")[:-1]

    if len(domain_name) > 1:
        raise NotImplementedError("Currently, this script is not able to " +
                                  "handle subdomains (or TLDs with multiple " +
                                  "prefixes). Please try again.")
    else:
        domain_name = domain_name[0]

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


def get_domain_dns(domain):
    """Get the DNS record, if any, for the given domain."""
    dns_records = list()

    try:
        # get the dns resolutions for this domain
        dns_results = dns.resolver.query(domain)
        dns_records = [ip.address for ip in dns_results]
    except dns.resolver.NXDOMAIN as e:
        # the domain does not exist so dns resolutions will remain None
        pass

    return dns_records


def output_possible_domain_squats(possible_domain_squats, real_domain_name,
                                  tld, charsets_used, dns_query,
                                  output_file=None):
    """Display each of the possible, internationalized domain squats."""
    output_json = dict()
    output_json[CURRENT_DATETIME] = dict()
    output_json[CURRENT_DATETIME]["{}.".format(real_domain_name) +
                                  "{}".format(tld)] = dict()
    output_json[CURRENT_DATETIME]['character_set_version'] = CHAR_SET_VERSION
    output_json[CURRENT_DATETIME]['fuzzer_version'] = FUZZER_VERSION

    current_location = output_json[CURRENT_DATETIME]["{}.{}".format(
        real_domain_name, tld)]
    current_location['character_sets'] = charsets_used
    current_location['possible_squats'] = list()
    possible_squats_list = current_location['possible_squats']
    current_location['results'] = len(possible_domain_squats)

    for squat in possible_domain_squats:
        domain_dict = dict()
        punycode_domain_name = "xn--{}.{}".format(
            str(squat.encode("punycode").decode("utf-8")), tld)
        if dns_query:
            domain_dns = [dns_record for dns_record in set(get_domain_dns(
                punycode_domain_name))]
            domain_dict['dns'] = domain_dns
            time.sleep(10)

        domain_dict['displayed'] = "{}.{}".format(squat, tld)
        # domain_dict['displayed'] = u"" + squat + "." + tld
        domain_dict['punycode'] = punycode_domain_name

        possible_squats_list.append(domain_dict)

    if output_file is not None:
        # write the output to a file
        with open(output_file, 'w+') as f:
            json.dump(output_json, f, indent=4, sort_keys=True)
            f.close()
    else:
        # print the output
        print(json.dumps(output_json, indent=4, sort_keys=True))


def main():
    """Find the internationalized domain squats for a given domain."""
    # parse the arguments
    args = init_parser()

    SPOOFABLE_CHARS, charsets_used = get_spoofable_charset(args)

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

    print("Found {} combinations\n".format(len(combinations)))

    # create each domain squat
    possible_domain_squats = get_possible_domain_squats(domain_name,
                                                        combinations,
                                                        SPOOFABLE_CHARS)

    # display each possible domain squat
    output_possible_domain_squats(possible_domain_squats, domain_name, tld,
                                  charsets_used, args.dns, args.output)


if __name__ == '__main__':
    main()
