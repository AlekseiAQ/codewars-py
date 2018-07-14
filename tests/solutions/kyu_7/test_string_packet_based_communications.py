"""String Packet Based Communications"""

import pytest

from solutions.kyu_7.string_packet_based_communications import communication_module

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("H1H10F1200120008F4F4", "H1H1FFFF00200000F4F4"),
        ("X7X7B7A201400058L0L0", "X7X7FFFF00820000L0L0"),
        ("R5R5C3D900120008K4K4", "R5R5FFFF00960000K4K4"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert communication_module(arg) == expected
