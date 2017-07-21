"""What century is it?
https://www.codewars.com/kata/what-century-is-it

Return the inputted numerical year in century format. For example 2014, would return ```21st```.

The input will always be a 4 digit string. So there is no need for year string validation<br />

Examples:<br />
Input: ```1999``` Output: ```20th```<br />
Input: ```2011``` Output: ```21st```<br />
Input: ```2154``` Output: ```22nd```<br />
Input: ```2259``` Output: ```23rd```<br />
Input: ```1124``` Output: ```12th```<br />
Input: ```2000``` Output: ```20th```<br />
"""


ENDINGS = {
    1: "st",
    2: "nd",
    3: "rd",
}


def whatCentury(year):
    """ what_century == PEP8 (forced mixedCase by CodeWars) """
    century = str((int(year) + 99) // 100)
    ending = "th" if 10 < int(century) < 20 else ENDINGS.get(int(century[-1]), "th")
    return century + ending
