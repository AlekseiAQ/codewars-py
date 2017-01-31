"""Regex Failure - Bug Fixing #2
https://www.codewars.com/kata/regex-failure-bug-fixing-number-2

<h1>Regex Failure - Bug Fixing #2</h1>
Oh no, Timmy's received some hate mail recently but he knows better. Help Timmy fix his regex filter so he can be awesome again!

"""


import re


def filter_words(phrase):
    return re.sub("(bad|mean|ugly|horrible|hideous)", "awesome", phrase, flags=re.I)
