"""Simple elevator"""

import pytest

from solutions.kyu_7.simple_elevator import goto

EXAMPLES = (
    ('args', 'expected'),
    [
        ((0, '2'), 2),
        ((4, '0'), 0),
        (([], '2'), 0),
        ((3, {}), 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert goto(*args) == expected
