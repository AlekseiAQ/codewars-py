"""Who Took The Car Key?"""

import pytest

from solutions.kyu_7.who_took_the_car_key import who_took_the_car_key

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['01000001', '01101100', '01100101', '01111000', '01100001',
          '01101110', '01100100', '01100101', '01110010'],
            'Alexander'),
        (['01001010', '01100101', '01110010', '01100101', '01101101',
          '01111001'],
            'Jeremy'),
        (['01000011', '01101000', '01110010', '01101001', '01110011'],
            'Chris'),
        (['01001010', '01100101', '01110011', '01110011', '01101001',
          '01100011', '01100001'],
            'Jessica'),
        (['01001010', '01100101', '01110010', '01100101', '01101101',
          '01111001'],
            'Jeremy'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert who_took_the_car_key(arg) == expected
