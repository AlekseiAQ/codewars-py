"""Perfect squares,  perfect fun"""

import pytest

from solutions.kyu_7.perfect_squares_perfect_fun import square_it

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, "1"),
        (222, "Not a perfect square!"),
        (234562342342, "Not a perfect square!"),
        (88989, "Not a perfect square!"),
        (112141568, "112\n141\n568"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert square_it(arg) == expected
