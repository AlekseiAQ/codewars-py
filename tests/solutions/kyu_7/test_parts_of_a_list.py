"""Parts of a list"""

import pytest

from solutions.kyu_7.parts_of_a_list import partlist

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["I", "wish", "I", "hadn't", "come"],
            [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"), ("I wish I hadn't", "come")]),
        (["cdIw", "tzIy", "xDu", "rThG"], 
            [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")]),
        (["vJQ", "anj", "mQDq", "sOZ"], 
            [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert partlist(arg) == expected
