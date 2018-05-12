"""Counting Array Elements"""

import pytest

from solutions.kyu_7.counting_array_elements import count

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['a', 'a', 'b', 'b', 'b'], {'a': 2, 'b': 3})
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert count(arg) == expected
