"""Multiplication - Generators #2"""

import pytest

from solutions.kyu_7.multiplication_generators_number_2 import generator

GEN = generator(1)
EXAMPLES = (
    ("arg", "expected"),
    [
        (next(GEN), "1 x 1 = 1"),
        (next(GEN), "1 x 2 = 2"),
        (next(GEN), "1 x 3 = 3"),
        (next(GEN), "1 x 4 = 4"),
        (next(GEN), "1 x 5 = 5"),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
