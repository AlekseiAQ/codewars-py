"""Indexed capitalization"""

import pytest

from solutions.kyu_7.indexed_capitalization import capitalize

EXAMPLES = (
    ('args', 'expected'),
    [
        (("abcdef", [1, 2, 5]), 'aBCdeF'),
        (("abcdef", [1, 2, 5, 100]), 'aBCdeF',),
        (("codewars", [1, 3, 5, 50]), 'cOdEwArs'),
        (("abracadabra", [2, 6, 9, 10]), 'abRacaDabRA'),
        (("codewarriors", [5]), 'codewArriors'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert capitalize(*args) == expected
