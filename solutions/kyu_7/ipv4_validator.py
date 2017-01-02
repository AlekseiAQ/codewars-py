"""IPv4 Validator
https://www.codewars.com/kata/ipv4-validator

In this kata you have to write a method to verify the validity of IPv4 addresses.

Example of valid inputs:

"1.1.1.1"

"127.0.0.1"

"255.255.255.255"

Example of invalid input:

"1444.23.9"

"153.500.234.444"

"-12.344.43.11"
"""


import re


def ip_validator(ip):
    return bool(re.match(r'^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$', ip))
