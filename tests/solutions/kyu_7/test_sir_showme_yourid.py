"""Sir , showMe  yourID """

import pytest

from solutions.kyu_7.sir_showme_yourid import show_me

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Francis", True),
        ("Jean-Eluard", True),
        ("Le Mec", False),
        ("Bernard-Henry-Levy", True),
        ("Meme Gertrude", False),
        ("A-a-a-a----a-a", False),
        ("Z-------------", False),
        ("Jean-luc", False),
        ("Jean--Luc", False),
        ("JeanLucPicard", False),
        ("-Jean-Luc", False),
        ("Jean-Luc-Picard-", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert show_me(arg) == expected
