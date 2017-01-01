"""Do I get a bonus?"""

import pytest

from solutions.kyu_8.do_i_get_a_bonus import bonus_time

EXAMPLES = (
    ('args', 'expected'),
    [
        ((10000, True), '$100000'),
        ((25000, True), '$250000'),
        ((10000, False), '$10000'),
        ((60000, False), '$60000'),
        ((2, True), '$20'),
        ((78, False), '$78'),
        ((67890, True), '$678900'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert bonus_time(*args) == expected
