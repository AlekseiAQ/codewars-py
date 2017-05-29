"""Adding values of arrays in a shifted way"""

import pytest

from solutions.kyu_7.adding_values_of_arrays_in_a_shifted_way import sum_arrays

EXAMPLES = (
    ('args', 'expected'),
    [
        (([[1, 2, 3, 4, 5, 6], [7, 7, 7, 7, 7, -7]], 0),
            [8, 9, 10, 11, 12, -1]),
        (([[1, 2, 3, 4, 5, 6], [7, 7, 7, 7, 7, 7 ]], 3),
            [1, 2, 3, 11, 12, 13, 7, 7, 7]),
        (([[1, 2, 3, 4, 5, 6], [7, 7, 7, -7, 7, 7], [1, 1, 1, 1, 1, 1]], 3),
            [1, 2, 3, 11, 12, 13, -6, 8, 8, 1, 1, 1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sum_arrays(*args) == expected
