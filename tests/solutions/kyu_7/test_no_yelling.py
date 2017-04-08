"""No yelling!"""

import pytest

from solutions.kyu_7.no_yelling import filter_words

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('HELLO world!', 'Hello world!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert filter_words(arg) == expected
