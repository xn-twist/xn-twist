#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# September 2016
# Licensed with MIT License (see the LICENSE file)
"""Find internationalized domain squats of a given domain."""


import argparse
import itertools
import urllib.parse


SPOOFABLE_CHARS = {
    'a': []
}


def init_parser():
    """Initialize the argument parser."""
    parser = argparse.ArgumentParser(description='Find internationalized ' +
                                                 'domain squats.')
    parser.add_argument('domain', metavar='domain', type=str, nargs=1,
                        help='A domain for which to find domain squats.')

    return parser.parse_args()


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


def get_possible_domain_squats(domain_name, combinations):
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

    # get the domain from which we should look for domain squats
    domain_name, tld = get_domain_details(args.domain[0])

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
                                                        combinations)

    # display each possible domain squat
    display_possible_domain_squats(possible_domain_squats, tld)


if __name__ == '__main__':
    main()
