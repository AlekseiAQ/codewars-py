"""Welcome!"""

import pytest

from solutions.kyu_8.welcome import greet

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('english', 'Welcome'),
        ('dutch', 'Welkom'),
        ('IP_ADDRESS_INVALID', 'Welcome'),
        ('', 'Welcome'),
        (2, 'Welcome'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert greet(arg) == expected
