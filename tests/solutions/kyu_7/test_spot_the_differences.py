"""Spot the Differences"""

import pytest

from solutions.kyu_7.spot_the_differences import spot_diff

EXAMPLES = (
    ('args', 'expected'),
    [
        (('abcdefg', 'abcqetg'), [3, 5]),
        (('Hello World!', 'hello world.'), [0, 6, 11]),
        (('FixedGrey', 'FixedGrey'), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert spot_diff(*args) == expected
