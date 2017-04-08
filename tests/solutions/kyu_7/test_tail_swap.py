"""Tail Swap"""

import pytest

from solutions.kyu_7.tail_swap import tail_swap

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['abc:123', 'cde:456'], ['abc:456', 'cde:123']),
        (['a:12345', '777:xyz'], ['a:xyz', '777:12345']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert tail_swap(arg) == expected
