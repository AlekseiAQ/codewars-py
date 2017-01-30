"""Complete The Pattern #8 - Number Pyramid"""

import pytest

from solutions.kyu_6.complete_the_pattern_number_8_number_pyramid import make_line, pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (4,"   1   \n  121  \n 12321 \n1234321"),
        (0,""),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
