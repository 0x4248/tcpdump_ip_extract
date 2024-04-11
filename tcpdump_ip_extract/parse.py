# Tcpdump ip extract
# Parse IP addresses from a tcpdump file
# Github: https://www.github.com/0x4248/tcpdump_ip_extract
# License: GNU General Public License v3.0
# By: 0x4248

import re

def extract_ipv4_address(string):
    ips = []
    for line in string.splitlines():
        ip_address = re.search(r'(?<!\.)\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', line)
        if ip_address:
            ips.append(ip_address.group(0))
    return ips

def extract_ipv6_address(string):
    ips = []
    for line in string.splitlines():
        ip_address = re.search(r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))', line)
        if ip_address:
            ips.append(ip_address.group(0))
    return ips

def ipv6_length_filter(ips):
    return [ip for ip in ips if len(ip) > 15]

def remove_duplicates(ips):
    return list(set(ips))