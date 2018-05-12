"""User class for Banking System"""

import pytest

from solutions.kyu_7.user_class_for_banking_system import User

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

EXAMPLES = (
    ('arg', 'expected'),
    [
        (Jeff.withdraw(2), 'Jeff has 68.'),
        (Joe.check(Jeff, 50), 'Joe has 120 and Jeff has 18.'),
        (Jeff.check(Joe, 80), 'Jeff has 98 and Joe has 40.'),
        (Jeff.add_cash(20), 'Jeff has 118.'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
