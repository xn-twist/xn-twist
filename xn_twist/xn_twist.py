#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# This project is licensed under an MIT License.
"""Find Unicode domain squats of a given domain."""


import argparse
import datetime
import itertools
import json
import time

import dns.resolver
import tldextract
from xntwist_python_sdk import xntwist_python_sdk


CURRENT_DATETIME = str(datetime.datetime.today())
# TODO: implement the char-set-version on the API/sdk
CHAR_SET_VERSION = '0.1'
FUZZER_VERSION = '1.0.0'


def init_parser():
    """Initialize the argument parser."""
    parser = argparse.ArgumentParser(description='Find Unicode ' +
                                                 'domain squats.')

    # get domain from which internationalized domains squats will be derived
    parser.add_argument('domain', help='domain name from which to search')

    # other configurations
    parser.add_argument('-d', '--dns', action='store_true',
                        help='query DNS for each domain')
    parser.add_argument('-o', '--output', nargs='?',
                        help='path to file to which results will be written')

    return parser.parse_args()


def get_spoofable_charset():
    """Retrieve and return the data from the desired character sets."""
    # instantiate an instance of the XN-Twist Python SDK
    xn_sdk = xntwist_python.XnTwistSDK()

    # pull the data from the API
    dataset = xn_sdk.retrieve_dataset()

    return dataset


def get_domain_details(domain):
    """Return the domain name and the top level domain (tld)."""
    parsed_domain = tldextract.extract(domain)

    if parsed_domain.subdomain:
        print("Currently, subdomains are not twisted and will be ignored. " +
              "If you'd like to see this functionality added, let me know " +
              "here: https://github.com/xn-twist/xn-twist/issues/17.")

    return parsed_domain.domain, parsed_domain.suffix


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
                                  domain_suffix, dns_query, output_file=None):
    """Display each of the possible, internationalized domain squats."""
    output_json = dict()
    output_json[CURRENT_DATETIME] = dict()
    output_json[CURRENT_DATETIME]["{}.".format(real_domain_name) +
                                  "{}".format(domain_suffix)] = dict()
    output_json[CURRENT_DATETIME]['character_set_version'] = CHAR_SET_VERSION
    output_json[CURRENT_DATETIME]['fuzzer_version'] = FUZZER_VERSION

    current_location = output_json[CURRENT_DATETIME]["{}.{}".format(
        real_domain_name, domain_suffix)]
    current_location['possible_squats'] = list()
    possible_squats_list = current_location['possible_squats']
    current_location['results'] = len(possible_domain_squats)

    for squat in possible_domain_squats:
        domain_dict = dict()
        punycode_domain_name = "xn--{}.{}".format(
            str(squat.encode("punycode").decode("utf-8")), domain_suffix)
        if dns_query:
            domain_dns = [dns_record for dns_record in set(get_domain_dns(
                punycode_domain_name))]
            domain_dict['dns'] = domain_dns
            time.sleep(10)

        domain_dict['displayed'] = "{}.{}".format(squat, domain_suffix)
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

    SPOOFABLE_CHARS = get_spoofable_charset()

    # get the domain from which we should look for domain squats
    domain_name, domain_suffix = get_domain_details(args.domain)

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
    output_possible_domain_squats(possible_domain_squats, domain_name,
                                  domain_suffix, args.dns, args.output)


if __name__ == '__main__':
    main()
