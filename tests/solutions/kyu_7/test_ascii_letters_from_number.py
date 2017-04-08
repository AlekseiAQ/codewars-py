"""ASCII letters from Number"""

import pytest

from solutions.kyu_7.ascii_letters_from_number import convert

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("65","A"),
        ("656667","ABC"),
        ("676584","CAT"),
        ("73327673756932858080698267658369","I LIKE UPPERCASE"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert convert(arg) == expected
