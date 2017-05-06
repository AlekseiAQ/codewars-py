"""Cat and Mouse - Easy Version"""

import pytest

from solutions.kyu_7.cat_and_mouse_easy_version import cat_mouse

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('C....m', "Escaped!"),
        ('C..m', "Caught!"),
        ('C.....m', "Escaped!"),
        ('C.m', "Caught!"),
        ('m...C', "Caught!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cat_mouse(arg) == expected
