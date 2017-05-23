"""PopShift"""

import pytest

from solutions.kyu_7.popshift import pop_shift

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("reusetestcasesbitcointakeovertheworldmaybewhoknowsperhaps", ["spahrepswonkohwebyamdlroweht","reusetestcasesbitcointakeove", "r"]),
        ("turnsoutrandomtestcasesareeasierthanwritingoutbasicones", ["senocisabtuognitirwnahtreis","turnsoutrandomtestcasesaree", "a"]),
        ("exampletesthere", ["erehtse","example","t"]),
        ("letstalkaboutjavascriptthebestlanguage", ["egaugnaltsebehttpir","letstalkaboutjavasc",""]),
        ("iwanttotraveltheworldwritingcodeoneday", ["yadenoedocgnitirwdl","iwanttotravelthewor",""]),
        ("letsallgoonholidaysomewhereverycold", ["dlocyreverehwemos","letsallgoonholida","y"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pop_shift(arg) == expected
