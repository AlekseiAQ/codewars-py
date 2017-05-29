"""ReOrdering"""

import pytest

from solutions.kyu_7.reordering import re_ordering

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('ming Yao', 'Yao ming'),
        ('Mano donowana', 'Mano donowana'),
        ('wario LoBan hello', 'LoBan wario hello'),
        ('bull color pig Patrick', 'Patrick bull color pig'),
        ('jojo ddjajdiojdwo ana G nnibiial',
            'G jojo ddjajdiojdwo ana nnibiial'),
        ('is one of those rare names that s both exotic and simple Adira',
            'Adira is one of those rare names that s both exotic and simple'),
        ('is an older name than annabel Amabel and a lot more distinctive',
            'Amabel is an older name than annabel and a lot more distinctive'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert re_ordering(arg) == expected
