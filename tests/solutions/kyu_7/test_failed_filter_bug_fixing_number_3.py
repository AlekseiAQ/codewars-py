"""Failed Filter - Bug Fixing #3"""

import pytest

from solutions.kyu_7.failed_filter_bug_fixing_number_3 import filter_numbers

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("test123", 'test'),
        ("a1b2c3", 'abc'),
        ("aa1bb2cc3dd", 'aabbccdd'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert filter_numbers(arg) == expected
