"""simple validation of a username with regex
https://www.codewars.com/kata/simple-validation-of-a-username-with-regex

Write a simple regex to validate a username.

Allowed characters are:

-lowercase letters
-numbers
-underscore

length shoould be between 4 and 16 characters.
"""


import re

def validate_usr(username):
    return bool(re.match(r"^[a-z0-9_]{4,16}$", username))
