"""String reverse slicing 101"""

import pytest

from solutions.kyu_7.string_reverse_slicing_101 import reverse_slice

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('123', ['321', '21', '1']),
        ('abcde', ['edcba', 'dcba', 'cba', 'ba', 'a']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_slice(arg) == expected
