"""Cut array into smaller parts"""

import pytest

from solutions.kyu_7.cut_array_into_smaller_parts import make_parts

EXAMPLES = (
    ('arr', 'chunksize', 'expected'),
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4],[5]]),
        ([1, 2, 3], 1, [[1], [2], [3]]),
        ([1, 2, 3, 4, 5], 10, [[1, 2, 3, 4, 5]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arr, chunksize, expected):
    assert make_parts(arr, chunksize) == expected
