"""String basics"""

import pytest

from solutions.kyu_7.string_basics import get_users_ids

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("uid12345", ["12345"]),
        ("   uidabc  ", ["abc"]),
        ("#uidswagger", ["swagger"]),
        ("uidone, uidtwo", ["one", "two"]),
        ("uidCAPSLOCK", ["capslock"]),
        ("uid##doublehashtag", ["doublehashtag"]),
        ("  uidin name whitespace", ["in name whitespace"]),
        ("uidMultipleuid", ["multipleuid"]),
        ("uid12 ab, uid#, uidMiXeDcHaRs", ["12 ab", "", "mixedchars"]),
        (" uidT#e#S#t# ", ["test"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_users_ids(arg) == expected
