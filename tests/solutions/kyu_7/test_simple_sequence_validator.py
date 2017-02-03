"""Simple Sequence Validator"""

import pytest

from solutions.kyu_7.simple_sequence_validator import validate_sequence

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 3, 4, 5, 8, 7, 8, 9], False),
        ([2, 8, 6, 7, 4, 3, 1, 5, 9], False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], True),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], True),
        ([1, 3, 5, 7, 9, 11, 13, 15], True),
        ([1, 3, 5, 7, 8, 12, 14, 16], False),
        ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate_sequence(arg) == expected
