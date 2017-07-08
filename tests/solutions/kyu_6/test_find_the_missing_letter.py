"""Find the missing letter"""

import pytest

from solutions.kyu_6.find_the_missing_letter import find_missing_letter

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['a', 'b', 'c', 'd', 'f'], 'e'),
        (['O', 'Q', 'R', 'S'], 'P'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_missing_letter(arg) == expected
