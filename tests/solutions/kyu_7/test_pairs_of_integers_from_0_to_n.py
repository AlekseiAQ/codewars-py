"""Pairs of integers from 0 to n"""

import pytest

from solutions.kyu_7.pairs_of_integers_from_0_to_n import generate_pairs

EXAMPLES = (
    ('arg', 'expected'),
    [
        (2, [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]]),
        (0, [[0, 0]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert generate_pairs(arg) == expected
