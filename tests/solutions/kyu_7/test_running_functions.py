"""Running functions"""

import pytest

from solutions.kyu_7.running_functions import running

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1,9,2,10], max), [1,9,9,10]),
        (([1,9,2,10], min), [1,1,1,1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert running(*args) == expected
