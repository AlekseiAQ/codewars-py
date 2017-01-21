"""Price of Mangoes"""

import pytest

from solutions.kyu_8.price_of_mangoes import mango

EXAMPLES = (
    ('args', 'expected'),
    [
        ((3, 3), 6),
        ((9, 5), 30),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert mango(*args) == expected
