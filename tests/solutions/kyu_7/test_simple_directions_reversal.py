"""Simple directions reversal"""

import pytest

from solutions.kyu_7.simple_directions_reversal import solve

EXAMPLES = (
    ("arg", "expected"),
    [
        (
            ["Begin on 3rd Blvd", "Right on First Road", "Left on 9th Dr"],
            ["Begin on 9th Dr", "Right on First Road", "Left on 3rd Blvd"],
        ),
        (
            ["Begin on Road A", "Right on Road B", "Right on Road C", "Left on Road D"],
            ["Begin on Road D", "Right on Road C", "Left on Road B", "Left on Road A"],
        ),
        (["Begin on Road A"], ["Begin on Road A"]),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
