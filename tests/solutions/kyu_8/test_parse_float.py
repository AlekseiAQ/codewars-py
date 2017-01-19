"""Parse float"""

import pytest

from solutions.kyu_8.parse_float import parse_float

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1.0", 1.0),
        ("a", None),
        ("234.0234", 234.0234),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert parse_float(arg) == expected
