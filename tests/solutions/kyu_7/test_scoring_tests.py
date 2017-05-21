"""Scoring Tests"""

import pytest

from solutions.kyu_7.scoring_tests import score_test

EXAMPLES = (
    ('args', 'expected'),
    [
        (([0, 0, 0, 0, 2, 1, 0], 2, 0, 1), 9),
        (([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2), 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert score_test(*args) == expected
