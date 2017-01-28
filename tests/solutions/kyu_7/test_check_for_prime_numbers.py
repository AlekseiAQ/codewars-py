"""Check for prime numbers"""

import pytest

from solutions.kyu_7.check_for_prime_numbers import is_prime

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0,False),
        (1,False),
        (2,True),
        (11,True),
        (12,False),
        (571,True),
        (25,False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_prime(arg) == expected
