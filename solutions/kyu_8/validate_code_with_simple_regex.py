"""validate code with simple regex
https://www.codewars.com/kata/validate-code-with-simple-regex

Basic regex tasks. Write a function that takes in a numeric code of any lenght. The function will check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise. 

You can assume the input will always be a nuber.
"""


import re


def validate_code(code):
    return re.match(r"^[1-3]+", str(code)) != None
