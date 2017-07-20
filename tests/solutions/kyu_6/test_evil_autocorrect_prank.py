"""Evil Autocorrect Prank"""

import pytest

from solutions.kyu_6.evil_autocorrect_prank import autocorrect

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("u", "your sister"),
        ("you", "your sister"),
        ("Youuuuu", "your sister"),
        ("youtube", "youtube"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert autocorrect(arg) == expected
