"""Zero Terminated Sum"""

import pytest

from solutions.kyu_7.zero_terminated_sum import largest_sum

EXAMPLES = (
    ("arg", "expected"),
    [("72102450111111090", 11), ("123004560", 15), ("0", 0)],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert largest_sum(arg) == expected
