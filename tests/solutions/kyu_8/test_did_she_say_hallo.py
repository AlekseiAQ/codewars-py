"""Did she say hallo?"""

import pytest

from solutions.kyu_8.did_she_say_hallo import validate_hello

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('hello', True),
        ('ciao bella!', True),
        ('salut', True),
        ('hallo, salut', True),
        ('hombre! Hola!', True),
        ('Hallo, wie geht\'s dir?', True),
        ('AHOJ!', True),
        ('czesc', True),
        ('meh', False),
        ('Ahoj', True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate_hello(arg) == expected
