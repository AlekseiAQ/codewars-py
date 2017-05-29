"""Ordered Count of Characters"""

import pytest

from solutions.kyu_7.ordered_count_of_characters import ordered_count

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('abracadabra',
            [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
        ('Code Wars',
            [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1),
             ('a', 1), ('r', 1), ('s', 1)]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert ordered_count(arg) == expected
