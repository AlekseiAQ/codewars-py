"""UVB-76 Message Validator"""

import pytest

from solutions.kyu_7.uvb_76_message_validator import validate

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Is this a right message?", False),
        ("MDZHB 85 596 KLASA 81 00 02 91", True),
        ("MDZHB 12 733 EDINENIE 67 79 66 32", True),
        ("MDZHV 60 130 VATRUKH 58 89 54 54", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate(arg) == expected
