"""N-th Power"""

import pytest

from solutions.kyu_8.n_th_power import index

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 2, 3, 4],2),9),
        (([1, 3, 10, 100],3),1000000),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert index(*args) == expected
