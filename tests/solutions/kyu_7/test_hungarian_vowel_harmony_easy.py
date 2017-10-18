"""Hungarian Vowel Harmony (easy)"""

import pytest

from solutions.kyu_7.hungarian_vowel_harmony_easy import dative

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("ablak", "ablaknak"),
        ("tükör", "tükörnek"),
        ("keret", "keretnek"),
        ("otthon", "otthonnak"),
        ("virág", "virágnak"),
        ("tett", "tettnek"),
        ("rokkant", "rokkantnak"),
        ("rossz", "rossznak"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert dative(arg) == expected
