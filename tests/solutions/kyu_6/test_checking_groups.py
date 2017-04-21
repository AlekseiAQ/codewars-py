"""Checking Groups"""

import pytest

from solutions.kyu_6.checking_groups import group_check

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("()", True),
        ("({", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert group_check(arg) == expected
