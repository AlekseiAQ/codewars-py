"""All Star Code Challenge #1"""

import pytest

from solutions.kyu_7.all_star_code_challenge_number_1 import sum_ppg

iverson = {'team': '76ers', 'ppg': 11.2}
jordan  = {'team': 'bulls', 'ppg': 20.2}

EXAMPLES = (
    ('args', 'expected'),
    [
        ((iverson, jordan), 31.4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sum_ppg(*args) == expected
