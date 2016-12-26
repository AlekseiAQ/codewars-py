"""Last"""

import pytest

from solutions.kyu_8.last import last

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1,2,3,4,5]), 5),
        (("abcde"), "e"),
        ((1, "b", 3, "d", 5), 5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert last(*args) == expected
