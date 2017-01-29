"""Genetic Algorithm Series - #1 Generate"""

import pytest

from solutions.kyu_7.genetic_algorithm_series_number_1_generate import generate

EXAMPLES = (
    ('arg', 'expected'),
    [
        (16, 16),
        (32, 32),
        (64, 64),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert len(generate(arg)) == expected
