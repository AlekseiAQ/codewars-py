"""Valid Phone Number"""

import pytest

from solutions.kyu_6.valid_phone_number import validPhoneNumber

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("(123) 456-7890", True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validPhoneNumber(arg) == expected
