"""Complete The Pattern #4"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_4 import pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (2,"12\n2"),
        (5,"12345\n2345\n345\n45\n5"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
