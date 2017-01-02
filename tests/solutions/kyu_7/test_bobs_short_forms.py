"""Bob's Short Forms"""

import pytest

from solutions.kyu_7.bobs_short_forms import short_form

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("assault", "asslt"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert short_form(arg) == expected
