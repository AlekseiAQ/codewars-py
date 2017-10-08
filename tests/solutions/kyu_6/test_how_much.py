"""How Much?"""

import pytest

from solutions.kyu_6.how_much import howmuch

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2950, 2950), []),
        ((20000, 20100), [["M: 20008", "B: 2858", "C: 2223"], ["M: 20071", "B: 2867", "C: 2230"]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert howmuch(*args) == expected
