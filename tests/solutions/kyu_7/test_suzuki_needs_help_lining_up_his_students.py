"""Suzuki needs help lining up his students!"""

import pytest

from solutions.kyu_7.suzuki_needs_help_lining_up_his_students import lineup_students

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi',
            ['Takehiko', 'Takayuki', 'Takahiro', 'Takeshi', 'Takeshi', 'Takashi', 'Tadashi', 'Takeo', 'Takao']),
        ('Shichiro Yoshiyuki Takeshi Yuichi Shigeo Shunichi Tamotsu',
            ['Yoshiyuki', 'Shunichi', 'Shichiro', 'Tamotsu', 'Takeshi', 'Yuichi', 'Shigeo']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert lineup_students(arg) == expected
