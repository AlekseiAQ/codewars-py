"""Love vs friendship"""

import pytest

from solutions.kyu_7.love_vs_friendship import words_to_marks

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('attitude', 100),
        ('friends', 75),
        ('family', 66),
        ('selfness', 99),
        ('knowledge', 96),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert words_to_marks(arg) == expected
