"""Complete The Pattern #9 - Diamond"""

import pytest

from solutions.kyu_6.complete_the_pattern_number_9_diamond import make_line, pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1,"1"),
        (3,"  1  \n 121 \n12321\n 121 \n  1  "),
        (7,"      1      \n     121     \n    12321    \n   1234321   \n  123454321  \n 12345654321 \n1234567654321\n 12345654321 \n  123454321  \n   1234321   \n    12321    \n     121     \n      1      "),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
