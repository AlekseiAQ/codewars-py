"""Dinner Plans"""

import pytest

from solutions.kyu_7.dinner_plans import common_ground

EXAMPLES = (
    ('args', 'expected'),
    [
        (("eat chicken", "eat chicken and rice"), 'eat chicken'),
        (("eat a burger and drink a coke", "drink a coke"), 'drink a coke'),
        (("i like turtles", "what are you talking about"), 'death'),
        (("aa bb", "aa bb cc"), "aa bb"),
        (("aa bb cc", "bb cc"), 'bb cc'),
        (("aa bb cc", "bb cc bb aa"), 'bb cc aa'),
        (("aa bb", "cc dd"), 'death'),
        (("aa bb", ""), 'death'),
        (("", "cc dd"), 'death'),
        (("", ""), 'death'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert common_ground(*args) == expected
