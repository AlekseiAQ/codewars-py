"""DigitAll"""

import pytest

from solutions.kyu_7.digitall import digit_all

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("are_you_kidding_me_???", ''),
        ("wai8, where are you goin'?", '8'),
        ("", ''),
        (['yes','i','am','kidding','you','!'], 'Invalid input !'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert digit_all(arg) == expected
