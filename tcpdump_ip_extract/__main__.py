# Tcpdump ip extract
# Parse IP addresses from a tcpdump file
# Github: https://www.github.com/lewisevans2007/tcpdump_ip_extract
# License: GNU General Public License v3.0
# By: Lewis Evans

import parse
import re
import argparse

try:
    from colorama import Fore, Back, Style
except ImportError:
    print('Please install colorama')
    exit()

def main():
    parser = argparse.ArgumentParser(description='Parse IP addresses from a tcpdump file', prog='tcpdump_ip_extract')
    parser.add_argument('-f', '--file', help='File to parse', required=True)
    parser.add_argument('-c', '--no-color', action='store_true', help='Disable color output')
    parser.add_argument('-n', '--number', action='store_true', help='Number output')
    parser.add_argument('-d', '--duplicate', action='store_true', help='Show duplicate IPs')
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            string = f.read()
    except FileNotFoundError:
        print('File not found')
        exit()

    if args.duplicate:
        ipv4_addresses = parse.extract_ipv4_address(string)
        ipv6_addresses = parse.extract_ipv6_address(string)
        ipv6_addresses = parse.ipv6_length_filter(ipv6_addresses)
    else:    
        ipv4_addresses = parse.remove_duplicates(parse.extract_ipv4_address(string))
        ipv6_addresses = parse.remove_duplicates(parse.extract_ipv6_address(string))
        ipv6_addresses = parse.ipv6_length_filter(ipv6_addresses)
    if args.number:
        print("Number\tIP Address")
    num = 1
    for ip in ipv4_addresses:
        if re.match(r"^192\.168\.\d{1,3}\.\d{1,3}$", ip) or re.match(r"^172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}$",ip):
            if args.no_color:
                if args.number:
                    print(str(num)+"\t"+ip)
                    num += 1
                else:
                    print(ip)
            else:
                if args.number:
                    print(str(num) + Fore.BLUE + "\t" + ip + Style.RESET_ALL)
                    num += 1
                else:
                    print(Fore.BLUE + ip)
        else:
            if args.no_color:
                if args.number:
                    print(str(num)+"\t"+ip)
                    num += 1
                else:
                    print(ip)
            else:
                if args.number:
                    print(str(num) + Fore.GREEN + "\t" + ip + Style.RESET_ALL)
                    num += 1
                else:
                    print(Fore.GREEN + ip)
    for ip in ipv6_addresses:
        if args.no_color:
            if args.number:
                print(str(num)+"\t"+ip)
                num += 1
            else:
                print(ip)
        else:
            if args.number:
                print(str(num) + Fore.MAGENTA + "\t" + ip + Style.RESET_ALL)
                num += 1
            else:
                print(Fore.MAGENTA + ip)

if __name__ == '__main__':
    main()
