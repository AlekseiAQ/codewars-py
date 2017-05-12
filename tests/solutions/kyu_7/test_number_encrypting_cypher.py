"""Number encrypting: cypher"""

import pytest

from solutions.kyu_7.number_encrypting_cypher import cypher

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hello World", "H3110 W0r1d"),
        ("I am your father", "1 4m y0ur f47h3r"),
        ("I do not know what else I can test. Be cool. Good luck", "1 d0 n07 kn0w wh47 3153 1 c4n 7357. 83 c001. 600d 1uck"),
        ("IlRzEeAaSsGbTtBgOo", "112233445566778900"),
        ("", ""),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cypher(arg) == expected
