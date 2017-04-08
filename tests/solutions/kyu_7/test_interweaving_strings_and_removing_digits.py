"""Interweaving strings and removing digits"""

import pytest

from solutions.kyu_7.interweaving_strings_and_removing_digits import interweave

EXAMPLES = (
    ('s1', 's2', 'expected'),
    [
        ("", "", ""),
        ("hlo", "el", 'hello'),
        ("h3lo", "el4", 'hello'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(s1, s2, expected):
    assert interweave(s1, s2) == expected
