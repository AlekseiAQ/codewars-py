"""Make acronym"""

import pytest

from solutions.kyu_7.make_acronym import to_acronym

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Code Wars", "CW"),
        ("Water Closet", "WC"),
        ("Portable Network Graphics", "PNG"),
        ("PHP: Hypertext Preprocessor", "PHP"),
        ("hyper text markup language", "HTML"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert to_acronym(arg) == expected
