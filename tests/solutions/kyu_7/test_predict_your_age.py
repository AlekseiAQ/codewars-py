"""Predict your age!"""

import pytest

from solutions.kyu_7.predict_your_age import predict_age

EXAMPLES = (
    ('args', 'expected'),
    [
        ((65, 60, 75, 55, 60, 63, 64, 45), 86)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert predict_age(*args) == expected
