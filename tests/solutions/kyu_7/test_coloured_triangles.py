"""Coloured Triangles"""

import pytest

from solutions.kyu_7.coloured_triangles import triangle

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('GB', 'R'),
        ('RRR', 'R'),
        ('RGBG', 'B'),
        ('RBRGBRB', 'G'),
        ('RBRGBRBGGRRRBGBBBGG', 'G'),
        ('B', 'B'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert triangle(arg) == expected
