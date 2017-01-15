"""Is there a vowel in there?"""

import pytest

from solutions.kyu_8.is_there_a_vowel_in_there import is_vow

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ],[118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]),
        ([101,121,110,113,113,103,121,121,101,107,103 ],["e",121,110,113,113,103,121,121,"e",107,103 ]),
        ([118,103,110,109,104,106 ],[118,103,110,109,104,106 ]),
        ([107,99,110,107,118,106,112,102 ],[107,99,110,107,118,106,112,102 ]),
        ([100,100,116,105,117,121 ],[100,100,116,"i","u",121 ]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_vow(arg) == expected
