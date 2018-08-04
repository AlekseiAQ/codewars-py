"""Single digit"""

import pytest

from solutions.kyu_7.single_digit import single_digit

EXAMPLES = (
    ('arg', 'expected'),
    [
        (5665, 5),
        (123456789, 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert single_digit(arg) == expected
