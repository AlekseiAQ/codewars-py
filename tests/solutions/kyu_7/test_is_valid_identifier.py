"""Is valid identifier?"""

import pytest

from solutions.kyu_7.is_valid_identifier import is_valid

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("okay_ok1", True),
        ("$ok", True),
        ("___", True),
        ("str_STR", True),
        ("myIdentf", True),
        ("1ok0okay", False),
        ("!Ok", False),
        ("", False),
        ("str-str", False),
        ("no no", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_valid(arg) == expected
