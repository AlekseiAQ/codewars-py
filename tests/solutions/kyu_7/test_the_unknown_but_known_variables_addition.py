"""The unknown but known variables: Addition"""

import pytest

from solutions.kyu_7.the_unknown_but_known_variables_addition import the_var

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('d+g', 11),
        ('a+a', 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert the_var(arg) == expected
