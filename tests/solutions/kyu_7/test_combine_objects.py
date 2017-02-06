"""Combine objects"""

import pytest

from solutions.kyu_7.combine_objects import combine

objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }
objC = { 'a': 5, 'd': 11, 'e': 8 }
objD = { 'c': 3 }

EXAMPLES = (
    ('args', 'expected'),
    [
        ((objA, objB), { 'a': 13, 'b': 20, 'c': 36, 'd': 3 }),
        ((objA, objC), { 'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8 }),
        ((objA, objB, objC), { 'a': 18, 'b': 20, 'c': 36, 'd': 14, 'e': 8 }),
        ((objA, objC, objD), { 'a': 15, 'b': 20, 'c': 33, 'd': 11, 'e': 8 }),
        (({}, {}, {}), {}),
        ((objA, objC, {}), { 'a': 15, 'b': 20, 'c': 30, 'd': 11, 'e': 8 }),
        (({}), {}),
        ((objA, objA, objA), { 'a': 30, 'b': 60, 'c': 90}),
        ((objD, objD, objD, objD, objD, objD), { 'c': 18}),
        ((objA, {}, objA), { 'a': 20, 'b': 40, 'c': 60}),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert combine(*args) == expected
