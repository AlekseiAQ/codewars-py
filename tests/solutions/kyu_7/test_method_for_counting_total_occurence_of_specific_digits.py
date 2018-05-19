"""Method For Counting Total Occurence Of Specific Digits"""

import pytest

from solutions.kyu_7.method_for_counting_total_occurence_of_specific_digits import \
    List

list_ = List()
[-18, -31, 81, -19, 111, -888]





EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3]),
         [(1, 3), (3, 2)]),
        (([-18, -31, 81, -19, 111, -888],  [1, 8, 4]),
         [(1, 7), (8, 5), (4, 0)]),
        (([-77, -65, 56, -79, 6666, 222], [1, 8, 4]),
          [(1, 0), (8, 0), (4, 0)]),
        (([],  [1, 8, 4]), 
         [(1, 0), (8, 0), (4, 0)]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert list_.count_spec_digits(*args) == expected
