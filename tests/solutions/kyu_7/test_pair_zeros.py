"""Pair Zeros"""

import pytest

from solutions.kyu_7.pair_zeros import pair_zeros

EXAMPLES = (
    ('args', 'expected'),
    [
        (([],), []),
        (([1],), [1]),
        (([1,2,3],), [1,2,3]),
        (([0],), [0]),
        (([0,0],), [0]),
        (([1,0,1,0,2,0,0],), [1,0,1,2,0]),
        (([0,0,0],), [0,0]),
        (([1,0,1,0,2,0,0,3,0],), [1,0,1,2,0,3,0]),
        (([1,0,1,0,2,0,0,3,0], 'some string', [1,2,3]), [1,0,1,2,0,3,0]),
        (([0,0,0,0,0,0,0,0,0,0,0,0],), [0,0,0,0,0,0]),
        (([0,0,0,0,0,0,0,0,0,0,0,0,0],), [0,0,0,0,0,0,0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert pair_zeros(*args) == expected
