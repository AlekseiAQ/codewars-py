"""MOD 256 without the MOD operator"""

import pytest

from solutions.kyu_7.mod_256_without_the_mod_operator import mod256_without_mod

EXAMPLES = (
    ('arg', 'expected'),
    [
        (254, 254),
        (256, 0),
        (258, 2),
        (-254, 2),
        (-256, 0),
        (-258, 254),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert mod256_without_mod(arg) == expected
