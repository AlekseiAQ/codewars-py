"""Hells Kitchen"""

import pytest

from solutions.kyu_7.hells_kitchen import gordon

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('What feck damn cake', 'WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!'),
        ('are you stu pid', '@R*!!!! Y**!!!! ST*!!!! P*D!!!!') ,
        ('i am a chef', '*!!!! @M!!!! @!!!! CH*F!!!!'),
        ('dont you talk tome', 'D*NT!!!! Y**!!!! T@LK!!!! T*M*!!!!') ,
        ('how dare you feck', 'H*W!!!! D@R*!!!! Y**!!!! F*CK!!!!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert gordon(arg) == expected
