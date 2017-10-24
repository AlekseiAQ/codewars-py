"""filterEvenLengthWords"""

import pytest

from solutions.kyu_7.filterevenlengthwords import filter_even_length_words

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["Hello", "World"], []),
        (["One", "Two", "Three", "Four"], ["Four"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert filter_even_length_words(arg) == expected
