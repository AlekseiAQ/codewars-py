"""Noonerize Me"""

import pytest

from solutions.kyu_7.noonerize_me import noonerize

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([12, 34], 18),
        ([55, 63], 12),
        ([357, 579], 178),
        ([1000000, 9999999], 7000001),
        ([1000000, "hello"], "invalid array"),
        (["pippi", 9999999], "invalid array"),
        (["pippi", "hello"], "invalid array"),
        ([1, 1], 0),
        ([1, 0], 1),
        ([0, 1], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert noonerize(arg) == expected
