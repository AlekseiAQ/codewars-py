"""Alternate capitalization"""

import pytest

from solutions.kyu_7.alternate_capitalization import capitalize

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("abcdef", ['AbCdEf', 'aBcDeF']),
        ("codewars", ['CoDeWaRs', 'cOdEwArS']),
        ("abracadabra", ['AbRaCaDaBrA', 'aBrAcAdAbRa']),
        ("codewarriors", ['CoDeWaRrIoRs', 'cOdEwArRiOrS']),
            ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert capitalize(arg) == expected
