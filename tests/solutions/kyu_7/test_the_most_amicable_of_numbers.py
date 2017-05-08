"""The Most Amicable of Numbers"""

import pytest

from solutions.kyu_7.the_most_amicable_of_numbers import amicable_numbers

EXAMPLES = (
    ('args', 'expected'),
    [
        ((220, 284), True),
        ((220, 280), False),
        ((1184, 1210), True),
        ((220221, 282224), False),
        ((10744, 10856), True),
        ((299920, 9284), False),
        ((999220, 2849), False),
        ((122265, 139815), True),
        ((220, 284), True),
        ((220, 284), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert amicable_numbers(*args) == expected
