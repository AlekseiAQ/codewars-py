"""To square(root) or not to square(root)"""

import pytest

from solutions.kyu_8.to_square_root_or_not_to_square_root import square_or_square_root

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([4, 3, 9, 7, 2, 1 ], [2, 9, 3, 49, 4, 1]),
        ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
        ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert square_or_square_root(arg) == expected
