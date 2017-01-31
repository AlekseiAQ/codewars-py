"""Gradually Adding Parameters"""

import pytest

from solutions.kyu_7.gradually_adding_parameters import add

EXAMPLES = (
    ('args', 'expected'),
    [
        ((100,200,300),1400),
        ((2,3),8),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert add(*args) == expected
