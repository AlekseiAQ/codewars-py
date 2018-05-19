"""Minumum and Maximum Product of k Elements"""

import pytest

from solutions.kyu_7.minumum_and_maximum_product_of_k_elements import \
    find_min_max_product

arr = [1, -2, -3, 4, 6, 7]

EXAMPLES = (
    ('args', 'expected'),
    [
        ((arr, 1), (-3, 7)),
        ((arr, 2), (-21, 42)),
        ((arr, 3), (-126, 168)),
        ((arr, 7), None),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert find_min_max_product(*args) == expected
