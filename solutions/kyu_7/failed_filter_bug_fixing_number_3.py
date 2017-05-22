"""Failed Filter - Bug Fixing #3
https://www.codewars.com/kata/failed-filter-bug-fixing-number-3

<h1>Failed Filter - Bug Fixing #3</h1>
Oh no, Timmy's filter doesn't seem to be working? Your task is to fix the FilterNumber function to remove all the numbers from the string.

"""


def filter_numbers(strng):
    return "".join(x for x in strng if not x.isdigit())
