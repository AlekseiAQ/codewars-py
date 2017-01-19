"""Freudian translator """

import pytest

from solutions.kyu_8.freudian_translator import to_freud

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("test", "sex"),
        ("sexy sex", "sex sex"),
        ("This is a test", "sex sex sex sex" ),
        ("This is a longer test", "sex sex sex sex sex" ),
        ("You're becoming a true freudian expert", "sex sex sex sex sex sex" ),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert to_freud(arg) == expected
