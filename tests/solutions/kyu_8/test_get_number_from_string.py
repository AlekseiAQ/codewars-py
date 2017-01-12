"""Get number from string"""

import pytest

from solutions.kyu_8.get_number_from_string import get_number_from_string

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1", 1),
        ("123", 123),
        ("this is number: 7", 7),
        ("$100 000 000", 100000000),
        ("hell5o wor6ld", 56),
        ("one1 two2 three3 four4 five5", 12345),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_number_from_string(arg) == expected
