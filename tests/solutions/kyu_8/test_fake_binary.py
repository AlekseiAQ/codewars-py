"""Fake Binary"""

import pytest

from solutions.kyu_8.fake_binary import fake_bin

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("45385593107843568", "01011110001100111"),
        ("509321967506747", "101000111101101"),
        ("366058562030849490134388085", "011011110000101010000011011"),
        ("15889923", "01111100"),
        ("800857237867", "100111001111"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert fake_bin(arg) == expected
