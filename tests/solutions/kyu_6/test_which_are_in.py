"""Which are  in?"""

import pytest

from solutions.kyu_6.which_are_in import in_array

EXAMPLES = (
    ('array1', 'array2', 'expected'),
    [
        (["live", "arp", "strong"],
        ["lively", "alive", "harp", "sharp", "armstrong"],
        ['arp', 'live', 'strong']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(array1, array2, expected):
    assert in_array(array1, array2) == expected
