"""Complete The Pattern #10 - Parallelogram"""

import pytest

from solutions.kyu_7.complete_the_pattern_number_10_parallelogram import make_line, pattern

EXAMPLES = (
    ('arg', 'expected'),
    [
        (3,"  123\n 123 \n123  "),
        (5,"    12345\n   12345 \n  12345  \n 12345   \n12345    "),
        (8,"       12345678\n      12345678 \n     12345678  \n    12345678   \n   12345678    \n  12345678     \n 12345678      \n12345678       "),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pattern(arg) == expected
