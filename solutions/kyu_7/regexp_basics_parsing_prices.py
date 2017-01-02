"""Regexp basics - parsing prices
https://www.codewars.com/kata/regexp-basics-parsing-prices

Implement `String#to_cents`, which should parse prices expressed as `$1.23` and return number of cents, or in case of bad format return `nil`.
"""


import re


def to_cents(amount):
    match = re.match(r'\$(\d+)\.(\d\d)\Z', amount)
    return int(match.expand(r'\1\2')) if match else None
