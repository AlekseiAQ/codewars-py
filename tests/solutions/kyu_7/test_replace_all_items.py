"""Replace all items"""

import pytest

from solutions.kyu_7.replace_all_items import replace_all

EXAMPLES = (
    ('args', 'expected'),
    [
        (([], 1, 2), []),
        (([1, 2, 2], 1, 2), [2, 2, 2]),
        (([1, 1, 2], 1, 2), [2, 2, 2]),
        (([1, 2, 1, 2, 3], 1, 2), [2, 2, 2, 2, 3]),
        (("Hello World", 'o', '0'), "Hell0 W0rld"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert replace_all(*args) == expected
