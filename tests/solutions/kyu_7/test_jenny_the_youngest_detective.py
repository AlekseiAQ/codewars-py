"""Jenny the youngest detective"""

import pytest

from solutions.kyu_7.jenny_the_youngest_detective import missing

EXAMPLES = (
    ('args', 'expected'),
    [
        (([5, 0, 3], "I love you"), "ivy"),
        (([29, 31, 8], "The quick brown fox jumps over the lazy dog"), "bay"),
        (([12, 4, 6], "Good Morning"), "No mission today"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert missing(*args) == expected
