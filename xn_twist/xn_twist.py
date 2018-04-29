#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# This project is licensed under an MIT License.
"""Find Unicode domain squats of a given domain."""

import datetime
import itertools
import json
import time

import dns.resolver
import tldextract
from xn_twist_python_sdk import xn_twist_python

CURRENT_DATETIME = str(datetime.datetime.today())
DEFAULT_LIMIT = 5


class XNTwist(object):
    """XNTwist class for finding Unicode domain-squats of a domain."""
    def __init__(self, query_dns=False, output=None):
        self.dns = query_dns
        self.output = output
        self.spoofable_chars = list()
        self.limit = DEFAULT_LIMIT

        # instantiate an instance of the XN-Twist Python SDK
        self.xn_sdk = xn_twist_python.XnTwistSDK()

    @staticmethod
    def _get_domain_details(domain):
        """Return the domain name and the top level domain (tld)."""
        parsed_domain = tldextract.extract(domain)

        if parsed_domain.subdomain:
            print("Currently, subdomains are not twisted and will be ignored. If you'd like to see this functionality added, let me know here: https://github.com/xn-twist/xn-twist/issues/17.")

        return parsed_domain.domain, parsed_domain.suffix

    @staticmethod
    def _get_combinations(index_list):
        """Get all combinations of the domain name's 'spoofable' indices."""
        return (combination
                for combination in itertools.chain.from_iterable(
                    itertools.combinations(index_list, i)
                    for i in range(1, len(index_list) + 1))
                )

    def _get_possible_squats(self, domain_name, combinations):
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
                    for spoofed_char in self.spoofable_chars[domain[index]]:
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

    @staticmethod
    def _get_domain_dns(domain):
        """Get the DNS record, if any, for the given domain."""
        dns_records = list()

        try:
            # get the dns resolutions for this domain
            dns_results = dns.resolver.query(domain)
            dns_records = [ip.address for ip in dns_results]
        except dns.resolver.NXDOMAIN as e:
            # the domain does not exist so dns resolutions remain empty
            pass
        except dns.resolver.NoAnswer as e:
            # the resolver is not answering so dns resolutions remain empty
            pass

        return dns_records

    def _output_possible_domain_squats(self, possible_domain_squats, real_domain_name, domain_suffix):
        """Display each of the possible, internationalized domain squats."""
        output_json = dict()
        output_json['possible_squats'] = list()
        possible_squats_list = output_json['possible_squats']
        # add a count of the results
        output_json['count'] = len(possible_domain_squats)
        # add the datetimestamp
        output_json['datetime'] = CURRENT_DATETIME
        # add the xn-twist version number
        output_json['xn_twist_version'] = XN_TWIST_VERSION

        for squat in possible_domain_squats:
            domain_dict = dict()
            punycode_domain_name = "xn--{}.{}".format(
                str(squat.encode("punycode").decode("utf-8")), domain_suffix)
            if self.dns:
                dns_ips = set(self._get_domain_dns(punycode_domain_name))
                domain_dns = [dns_record for dns_record in dns_ips]
                domain_dict['dns'] = domain_dns
                time.sleep(10)

            domain_dict['displayed'] = "{}.{}".format(squat, domain_suffix)
            # domain_dict['displayed'] = u"" + squat + "." + tld
            domain_dict['punycode'] = punycode_domain_name

            possible_squats_list.append(domain_dict)

        if self.output is not None:
            # write the output to a file
            with open(self.output, 'w+') as f:
                json.dump(output_json, f, indent=4, sort_keys=True)
                f.close()
        else:
            # print the output
            print(json.dumps(output_json, indent=4, sort_keys=True))

        return output_json

    def twist(self, domain, limit=DEFAULT_LIMIT, simple=False):
        """Find the internationalized domain squats for a given domain."""
        # if the limit is changed, get a new dataset
        if limit != self.limit or len(self.spoofable_chars) == 0:
            self.spoofable_chars = self.xn_sdk.retrieve_dataset(limit=limit)

        # get the domain from which we should look for domain squats
        domain_name, domain_suffix = self._get_domain_details(domain)

        count = 0
        spoofable_indices = list()

        # find the index of each 'spoofable' character in the domain
        for char in domain_name:
            if char in self.spoofable_chars:
                spoofable_indices.append(count)

            count += 1

        # find all possible combinations of the 'spoofable' indices
        combinations = list(self._get_combinations(spoofable_indices))

        if simple:
            combinations = [combo for combo in combinations if len(combo) == 1]

        # create each domain squat
        possible_squats = self._get_possible_squats(domain_name, combinations)

        print("Found {} potential squats\n".format(len(possible_squats)))

        # display each possible domain squat
        output_json = self._output_possible_domain_squats(possible_squats, domain_name, domain_suffix)

        # return the results
        return output_json


# this import needs to come after the declaration of the `XNTwist` class so that __init__.py can import the XNTwist before this file tries to get the version from __init__.py
from .__init__ import __version__ as XN_TWIST_VERSION
