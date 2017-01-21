"""Squash the bugs"""

import pytest

from solutions.kyu_8.squash_the_bugs import find_longest

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("The quick white fox jumped around the massive dog", 7),
        ("Take me to tinseltown with you", 10),
        ("Sausage chops", 7),
        ("Wind your body and wiggle your belly", 6),
        ("Lets all go on holiday", 7),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_longest(arg) == expected
