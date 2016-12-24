"""Calculate String Rotation"""

import pytest

from solutions.kyu_6.calculate_string_rotation import shifted_diff

EXAMPLES = (
    ('args', 'expected'),
    [
        (("eecoff","coffee"), 4),
        (("Moose","moose"), -1),
        (("isn't","'tisn"), 2),
        (("Esham","Esham"), 0),
        ((" "," "), 0),
        (("hoop","pooh"), -1),
        (("  "," "), -1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert shifted_diff(*args) == expected
