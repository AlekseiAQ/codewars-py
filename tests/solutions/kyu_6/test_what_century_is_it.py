"""What century is it?"""

import pytest

from solutions.kyu_6.what_century_is_it import whatCentury

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1999", "20th"),
        ("1234", "13th")
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert whatCentury(arg) == expected
