"""Remove anchor from URL"""

import pytest

from solutions.kyu_6.remove_anchor_from_url import remove_url_anchor

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('www.codewars.com#about', 'www.codewars.com'),
        ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert remove_url_anchor(arg) == expected
