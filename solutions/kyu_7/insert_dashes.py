"""Insert dashes
https://www.codewars.com/kata/insert-dashes

Write a function `insertDash(num)`/`InsertDash(int num)` that will insert
dashes ('-') between each two odd numbers in num. For example: if num is 454793
the output should be 4547-9-3. Don't count zero as an odd number.
"""


import re


def insert_dash(num: int) -> str:
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
