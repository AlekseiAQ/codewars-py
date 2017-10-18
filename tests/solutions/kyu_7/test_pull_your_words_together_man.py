"""Pull your words together, man!"""

import pytest

from solutions.kyu_7.pull_your_words_together_man import sentencify

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["i", "am", "an", "AI"], "I am an AI."),
        (["yes"], "Yes."),
        (["FIELDS", "of", "CORN", "are", "to", "be", "sown"],
            "FIELDS of CORN are to be sown."),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sentencify(arg) == expected
