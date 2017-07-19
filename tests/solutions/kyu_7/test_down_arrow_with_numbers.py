"""Down Arrow With Numbers"""

import pytest

from solutions.kyu_7.down_arrow_with_numbers import get_a_down_arrow_of

EXAMPLES = (
    ('arg', 'expected'),
    [
        (10, "1234567890987654321\n 12345678987654321\n  123456787654321\n   1234567654321\n    12345654321\n     123454321\n      1234321\n       12321\n        121\n         1"),
        (0, ""),
        (-5, ""),
        (3, "12321\n 121\n  1"),
        (5, "123454321\n 1234321\n  12321\n   121\n    1"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_a_down_arrow_of(arg) == expected
