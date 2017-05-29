"""Describe a list """

import pytest

from solutions.kyu_7.describe_a_list import describeList

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([],"empty"),
        ([1],"singleton"),
        ([1,2,5,4],"longer"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert describeList(arg) == expected
