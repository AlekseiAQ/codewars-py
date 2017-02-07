"""Next Palindromic Number."""

import pytest

from solutions.kyu_7.next_palindromic_number import next_pal

EXAMPLES = (
    ('arg', 'expected'),
    [
        (11, 22),
        (188, 191),
        (191, 202),
        (2541, 2552),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert next_pal(arg) == expected
