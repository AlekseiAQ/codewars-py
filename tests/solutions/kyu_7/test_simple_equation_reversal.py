"""Simple equation reversal"""

import pytest

from solutions.kyu_7.simple_equation_reversal import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("100*b/y", "y/b*100"),
        ("a+b-c/d*30", "30*d/c-b+a"),
        ("a*b/c+50", "50+c/b*a"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
