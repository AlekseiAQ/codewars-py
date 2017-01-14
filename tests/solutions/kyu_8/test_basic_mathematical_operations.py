"""Basic Mathematical Operations"""

import pytest

from solutions.kyu_8.basic_mathematical_operations import basic_op

EXAMPLES = (
    ('args', 'expected'),
    [
        (('+', 4, 7), 11),
        (('-', 15, 18), -3),
        (('*', 5, 5), 25),
        (('/', 49, 7), 7),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert basic_op(*args) == expected
