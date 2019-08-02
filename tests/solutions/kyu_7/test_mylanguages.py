"""My Languages"""

import pytest

from solutions.kyu_7.mylanguages import my_languages

EXAMPLES = (
    ("arg", "expected"),
    [
        ({"Java": 10, "Ruby": 80, "Python": 65}, ["Ruby", "Python"]),
        ({"Hindi": 60, "Dutch": 93, "Greek": 71}, ["Dutch", "Greek", "Hindi"]),
        ({"C++": 50, "ASM": 10, "Haskell": 20}, []),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert my_languages(arg) == expected
