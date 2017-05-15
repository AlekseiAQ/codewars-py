"""Borrower Speak"""

import pytest

from solutions.kyu_7.borrower_speak import borrow

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('WhAt! FiCK! DaMn CAke?', 'whatfickdamncake'),
        ('THE big PeOpLE Here!!', 'thebigpeoplehere'),
        ('i AM a TINY BoY!!', 'iamatinyboy'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert borrow(arg) == expected
