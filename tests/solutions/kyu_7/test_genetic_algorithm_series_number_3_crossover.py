"""Genetic Algorithm Series - #3 Crossover"""

import pytest

from solutions.kyu_7.genetic_algorithm_series_number_3_crossover import crossover

EXAMPLES = (
    ('args', 'expected'),
    [
        (("110", "001", 2), ["111", "000"]),
        (("111000", "000110", 3), ["111110", "000000"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert crossover(*args) == expected
