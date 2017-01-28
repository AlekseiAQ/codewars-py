"""Unique Pairs"""

import pytest

from solutions.kyu_7.unique_pairs import projectPartners

EXAMPLES = (
    ('arg', 'expected'),
    [
        (2, 1),
        (3, 3),
        (4, 6),
        (5, 10),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert projectPartners(arg) == expected
