"""Unlucky Days"""

import pytest

from solutions.kyu_7.unlucky_days import unlucky_days

EXAMPLES = (
    ('arg', 'expected'),
    [
        (2015, 3),
        (1986, 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert unlucky_days(arg) == expected
