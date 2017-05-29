"""Find Duplicates """

import pytest

from solutions.kyu_7.find_duplicates import duplicates

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 4, 4, 3, 3, 1, 5, 3, '5'], [4,3,1]),
        ([0, 1, 2, 3, 4, 5], []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert duplicates(arg) == expected
