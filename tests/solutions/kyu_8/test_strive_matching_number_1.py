"""Strive Matching #1"""

import pytest


candidate1 = { 'min_salary': 120000 }
candidate2 = { 'min_salary': 190000 }
job1 = { 'max_salary': 130000 }
job2 = { 'max_salary': 80000 }
job3 = { 'max_salary': 171000 }


from solutions.kyu_8.strive_matching_number_1 import match

EXAMPLES = (
    ('args', 'expected'),
    [
        ((candidate1, job1), True),
        ((candidate1, job3), True),
        ((candidate2, job3), True),
        ((candidate1, job2), False),
        ((candidate2, job1), False),
        ((candidate2, job2), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert match(*args) == expected
