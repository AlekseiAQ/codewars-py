"""Complete The Pattern #6 - Odd Ladder"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_6_odd_ladder import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (4,"1\n333"),
        (1,"1"),
        (5,"1\n333\n55555"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
