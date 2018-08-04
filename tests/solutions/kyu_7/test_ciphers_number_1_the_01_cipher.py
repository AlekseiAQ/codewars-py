"""Ciphers #1 - The  01 Cipher"""

import pytest

from solutions.kyu_7.ciphers_number_1_the_01_cipher import encode

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hello World!","10110 00111!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert encode(arg) == expected
