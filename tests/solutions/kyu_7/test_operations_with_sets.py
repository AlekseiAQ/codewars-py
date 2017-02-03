"""Operations With Sets"""

import pytest

from solutions.kyu_7.operations_with_sets import process_2arrays

EXAMPLES = (
    ('arr1', 'arr2', 'expected'),
    [
        ([1, 2 ,3,4, 5 ,6 ,7 ,8 ,9],
         [2, 4, 6, 8, 10, 12, 14],
         [4, 8, 5, 3]),
        ([33, 2, 3, 37, 38, 40, 12, 10, 43, 44, 47, 49, 8, 19, 22, 24, 26, 28, 29, 30],
         [1, 34, 17, 7, 9, 10, 43, 49, 22, 27, 28],
         [5, 21, 15, 6]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arr1, arr2, expected):
    assert process_2arrays(arr1, arr2) == expected
