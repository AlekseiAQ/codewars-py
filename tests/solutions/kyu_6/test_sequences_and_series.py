"""Sequences and Series"""

import pytest

from solutions.kyu_6.sequences_and_series import get_score

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 50), 
        (2, 150),
        (3, 300),
        (4, 500),
        (5, 750),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_score(arg) == expected
