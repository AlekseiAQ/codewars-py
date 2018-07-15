"""Simple Fun #13: Magical Well"""

import pytest

from solutions.kyu_7.simple_fun_number_13_magical_well import magical_well

EXAMPLES = (
    ('args', 'expected'),
    [
        ((1, 2, 2), 8),
        ((1, 1, 1), 1),
        ((6, 5, 3), 128),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert magical_well(*args) == expected
