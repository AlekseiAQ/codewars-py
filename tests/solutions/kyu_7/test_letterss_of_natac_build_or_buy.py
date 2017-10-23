"""Letterss of natac: build or buy"""

import pytest

from solutions.kyu_7.letterss_of_natac_build_or_buy import build_or_buy

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("bwoo", ["road"]),
        ("", []),
        ("ogogoogogo", ["city"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert build_or_buy(arg) == expected
