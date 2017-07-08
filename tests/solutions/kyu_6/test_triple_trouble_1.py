"""Triple trouble"""

import pytest

from solutions.kyu_6.triple_trouble_1 import triple_double

EXAMPLES = (
    ('args', 'expected'),
    [
        ((451999277, 41177722899), 1),
        ((1222345, 12345), 0),
        ((12345, 12345), 0),
        ((666789, 12345667), 1),
        ((10560002, 100), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert triple_double(*args) == expected
