"""Spoonerize Me"""

import pytest

from solutions.kyu_7.spoonerize_me import spoonerize

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("nit picking", "pit nicking"),
        ("wedding bells", "bedding wells"),
        ("jelly beans", "belly jeans"),
        ("pop corn", "cop porn"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert spoonerize(arg) == expected
