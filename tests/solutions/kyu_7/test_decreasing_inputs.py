"""Decreasing  Inputs"""

import pytest

from solutions.kyu_7.decreasing_inputs import add

EXAMPLES = (
    ('args', 'expected'),
    [
        ((100,200,300),300),
        ((2,),2),
        ((4,-3,-2),2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert add(*args) == expected
