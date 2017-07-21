"""Simple Encryption #1 - Alternating Split"""

import pytest

from solutions.kyu_6.simple_encryption_number_1_alternating_split import \
    decrypt, encrypt

ENCRYPT_EXAMPLES = (
    ('args', 'expected'),
    [
        (("This is a test!", 0),
         "This is a test!"),
        (("This is a test!", 1),
         "hsi  etTi sats!"),
        (("This is a test!", 2),
         "s eT ashi tist!"),
        (("This is a test!", 3),
         " Tah itse sits!"),
        (("This is a test!", 4),
         "This is a test!"),
        (("This is a test!", -1),
         "This is a test!"),
        (("This kata is very interesting!", 1),
         "hskt svr neetn!Ti aai eyitrsig"),
    ]
)


@pytest.mark.parametrize(*ENCRYPT_EXAMPLES)
def test_returns_correct_result_for_encrypt(args, expected):
    assert encrypt(*args) == expected


DECRYPT_EXAMPLES = (
    ('args', 'expected'),
    [
        (("This is a test!", 0),
         "This is a test!"),
        (("hsi  etTi sats!", 1),
         "This is a test!"),
        (("s eT ashi tist!", 2),
         "This is a test!"),
        ((" Tah itse sits!", 3),
         "This is a test!"),
        (("This is a test!", 4),
         "This is a test!"),
        (("This is a test!", -1),
         "This is a test!"),
        (("hskt svr neetn!Ti aai eyitrsig", 1),
         "This kata is very interesting!"),
    ]
)


@pytest.mark.parametrize(*DECRYPT_EXAMPLES)
def test_returns_correct_result_for_decrypt(args, expected):
    assert decrypt(*args) == expected
