"""Triple Trouble"""

import pytest

from solutions.kyu_8.triple_trouble_2 import triple_trouble

EXAMPLES = (
    ('args', 'expected'),
    [
        (("aaa", "bbb", "ccc"), "abcabcabc"),
        (("aaaaaa", "bbbbbb", "cccccc"), "abcabcabcabcabcabc"),
        (("burn", "reds", "roll"), "brrueordlnsl"),
        (("Bm", "aa", "tn"), "Batman"),
        (("LLh", "euo", "xtr"), "LexLuthor"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert triple_trouble(*args) == expected
