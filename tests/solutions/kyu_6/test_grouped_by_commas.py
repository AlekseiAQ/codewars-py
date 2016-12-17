"""Grouped by commas"""

import pytest

from solutions.kyu_6.grouped_by_commas import group_by_commas

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, '1'),
        (10, '10'),
        (100, '100'),
        (1000, '1,000'),
        (10000, '10,000'),
        (100000, '100,000'),
        (1000000, '1,000,000'),
        (35235235, '35,235,235'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert group_by_commas(arg) == expected
