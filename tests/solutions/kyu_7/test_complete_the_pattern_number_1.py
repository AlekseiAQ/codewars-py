"""Complete The  Pattern #1 """

import pytest

from solutions.kyu_7.complete_the_pattern_number_1 import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (2,"1\n22"),
        (5,"1\n22\n333\n4444\n55555"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
