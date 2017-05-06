"""A Rule of Divisibility by 7"""

import pytest

from solutions.kyu_7.a_rule_of_divisibility_by_7 import seven

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1603, (7, 2)),
        (371, (35, 1)),
        (483, (42, 1)),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert seven(arg) == expected
