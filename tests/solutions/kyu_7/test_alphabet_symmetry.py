"""Alphabet symmetry"""

import pytest

from solutions.kyu_7.alphabet_symmetry import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["abode", "ABc", "xyzD"], [4, 3, 1]),
        (["abide", "ABc", "xyz"], [4, 3, 0]),
        (["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"], [6, 5, 7]),
        (["encode", "abc", "xyzD", "ABmD"], [1, 3, 1, 3]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
