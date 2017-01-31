"""Regex Failure - Bug Fixing #2"""

import pytest

from solutions.kyu_7.regex_failure_bug_fixing_number_2 import filter_words

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("You're Bad! timmy!","You're awesome! timmy!"),
        ("You're MEAN! timmy!","You're awesome! timmy!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert filter_words(arg) == expected
