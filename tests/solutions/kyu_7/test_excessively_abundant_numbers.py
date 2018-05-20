"""Excessively Abundant Numbers"""

import pytest

from solutions.kyu_7.excessively_abundant_numbers import abundant_number

EXAMPLES = (
    ('arg', 'expected'),
    [
        (12, True),
        (18, True),
        (37, False),
        (120, True),
        (77, False),
        (118, False),
        (5830, True),
        (11410, True),
        (14771, False),
        (11690, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert abundant_number(arg) == expected
