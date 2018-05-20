"""Simple string reversal"""

import pytest

from solutions.kyu_7.simple_string_reversal import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("codewars","srawedoc"),
        ("your code","edoc ruoy"),
        ("your code rocks","skco redo cruoy"),
        ("i love codewars","s rawe docevoli"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
