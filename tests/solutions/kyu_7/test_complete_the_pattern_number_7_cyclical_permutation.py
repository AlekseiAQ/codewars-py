"""Complete The Pattern #7 - Cyclical Permutation"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_7_cyclical_permutation import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (4,"1234\n2341\n3412\n4123"),
        (0,""),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
