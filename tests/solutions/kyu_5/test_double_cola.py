"""Double Cola"""

import pytest

from solutions.kyu_5.double_cola import whoIsNext

EXAMPLES = (
    ('args', 'expected'),
    [
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1), "Sheldon"),
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 2), "Leonard"),
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 3), "Penny"),
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 4), "Rajesh"),
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 5), "Howard"),
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 6), "Sheldon"),
        ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52), "Sheldon"),
        # ((["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951), "Leonard"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert whoIsNext(*args) == expected
