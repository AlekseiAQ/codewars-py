"""Lario and Muigi Pipe Problem"""

import pytest

from solutions.kyu_8.lario_and_muigi_pipe_problem import pipe_fix

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,5,6,8,9],[1,2,3,4,5,6,7,8,9]),
        ([1,2,3,12],[1,2,3,4,5,6,7,8,9,10,11,12]),
        ([6,9],[6,7,8,9]),
        ([-1,4],[-1,0,1,2,3,4]),
        ([1,2,3],[1,2,3]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pipe_fix(arg) == expected
