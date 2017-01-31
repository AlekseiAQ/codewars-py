"""Sort array by string length"""

import pytest

from solutions.kyu_7.sort_array_by_string_length import sort_by_length

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["beg", "life", "i", "to"], ["i", "to", "beg", "life"]),
        (["", "moderately", "brains", "pizza"], ["", "pizza", "brains", "moderately"]),
        (["longer", "longest", "short"], ["short", "longer", "longest"]),
        (["dog", "food", "a", "of"], ["a", "of", "dog", "food"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_by_length(arg) == expected
