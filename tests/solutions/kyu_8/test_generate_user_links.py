"""Generate user links"""

import pytest

from solutions.kyu_8.generate_user_links import generate_link

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('matt c', 'http://www.codewars.com/users/matt%20c'),
        ('g964', 'http://www.codewars.com/users/g964'),
        ('GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi'),
        ('ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra'),
        ('colbydauph', 'http://www.codewars.com/users/colbydauph'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert generate_link(arg) == expected
