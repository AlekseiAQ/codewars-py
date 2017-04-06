"""Find Multiples of a Number"""

import pytest

from solutions.kyu_8.find_multiples_of_a_number import find_multiples

EXAMPLES = (
    ('integer', 'limit', 'expected'),
    [
        (5, 25, [5, 10, 15, 20, 25]),
        (1, 2, [1, 2]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(integer, limit, expected):
    assert find_multiples(integer, limit) == expected
