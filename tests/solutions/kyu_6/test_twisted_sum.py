"""Twisted Sum"""

import pytest

from solutions.kyu_6.twisted_sum import compute_sum

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (10, 46),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert compute_sum(arg) == expected
