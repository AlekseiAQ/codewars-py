"""String cleaning"""

import pytest

from solutions.kyu_8.string_cleaning import string_clean

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", ""),
        ("! !", "! !"),
        ("123456789", ""),
        ("(E3at m2e2!!)", "(Eat me!!)"),
        ("Dsa32 cdsc34232 csa!!! 1I 4Am cool!", "Dsa cdsc csa!!! I Am cool!"),
        ("A1 A1! AAA   3J4K5L@!!!", "A A! AAA   JKL@!!!"),
        ("Adgre2321 A1sad! A2A3A4 fv3fdv3J544K5L@", "Adgre Asad! AAA fvfdvJKL@"),
        ("Ad2dsad3ds21 A  1$$s122ad! A2A3Ae24 f44K5L@222222 ", "Addsadds A  $$sad! AAAe fKL@ "),
        ("33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 ", "Addsadds A  $$sa!d! A!A!Ae$ f## "),
        ("My \"me3ssy\" d8ata issues2! Will1 th4ey ever, e3ver be3 so0lved?", "My \"messy\" data issues! Will they ever, ever be solved?"),
        ("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3", "Why can't we buy the good software? #cheapskates"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert string_clean(arg) == expected
