"""Rotate for a Max"""

import pytest

from solutions.kyu_7.rotate_for_a_max import max_rot

EXAMPLES = (
    ('arg', 'expected'),
    [
        (38458215, 85821534),
        (195881031, 988103115),
        (896219342, 962193428),
        (69418307, 94183076),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert max_rot(arg) == expected
