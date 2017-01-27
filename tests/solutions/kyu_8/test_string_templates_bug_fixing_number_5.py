"""String Templates - Bug Fixing #5"""

import pytest

from solutions.kyu_8.string_templates_bug_fixing_number_5 import build_string

EXAMPLES = (
    ('args', 'expected'),
    [
        (('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!'),
        (('Cheese','Milk'), 'I like Cheese, Milk!'),
        (('Chocolate',), 'I like Chocolate!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert build_string(*args) == expected
