"""International Morse Code Encryption"""

import pytest

from solutions.kyu_7.international_morse_code_encryption import encryption


EXAMPLES = (
    ('arg', 'expected'),
    [
        ("HELLO WORLD", ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."),
        ("SOS", "... --- ..."),
        ("1836", ".---- ---.. ...-- -...."),
        ("THE QUICK BROWN FOX", "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-"),
        ("JUMPED OVER THE", ".--- ..- -- .--. . -..   --- ...- . .-.   - .... ."),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert encryption(arg) == expected
