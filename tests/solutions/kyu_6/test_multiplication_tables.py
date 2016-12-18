"""Multiplication Tables"""

import pytest

from solutions.kyu_6.multiplication_tables import multiplication_table

EXAMPLES = (
    ('row', 'col', 'expected'),
    [
        (2,2, [[1,2],[2,4]]),
        (3,3, [[1,2,3],[2,4,6],[3,6,9]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(row, col, expected):
    assert multiplication_table(row, col) == expected
