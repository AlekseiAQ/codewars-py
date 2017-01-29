"""Compare Strings by Sum of Chars"""

import pytest

from solutions.kyu_7.compare_strings_by_sum_of_chars import compare

EXAMPLES = (
    ('s1', 's2', 'expected'),
    [
        ("AD", "BC", True),
        ("AD", "DD", False),
        ("gf", "FG", True),
        ("Ad", "DD", False),
        ("zz1", "", True),
        ("ZzZz", "ffPFF", True),
        ("kl", "lz", False),
        (None, "", True),
        ("!!", "7476", True),
        ("##", "1176", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(s1, s2, expected):
    assert compare(s1, s2) == expected
