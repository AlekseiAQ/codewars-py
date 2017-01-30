"""Complete The Pattern #5 - Even Ladder"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_5_even_ladder import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (2,"22"),
        (1,""),
        (5,"22\n4444"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
