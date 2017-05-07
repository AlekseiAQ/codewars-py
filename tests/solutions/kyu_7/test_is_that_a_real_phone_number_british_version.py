"""Is that a real phone number?  (British version)"""

import pytest

from solutions.kyu_7.is_that_a_real_phone_number_british_version import validate_number

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("07454876120", "In with a chance"),
        ("0754876120", "Plenty more fish in the sea"),
        ("0745--487-61-20", "In with a chance"),
        ("+447535514555", "In with a chance"),
        ("-07599-51-4555", "In with a chance"),
        ("075335440555", "Plenty more fish in the sea"),
        ("+337535512555", "Plenty more fish in the sea"),
        ("00535514555", "Plenty more fish in the sea"),
        ("+447+4435512555", "Plenty more fish in the sea"),
        ("+44", "Plenty more fish in the sea"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate_number(arg) == expected
