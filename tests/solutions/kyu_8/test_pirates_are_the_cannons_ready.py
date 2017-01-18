"""Pirates!! Are the Cannons ready!??"""

import pytest

from solutions.kyu_8.pirates_are_the_cannons_ready import cannons_ready

EXAMPLES = (
    ('arg', 'expected'),
    [
        ({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}, 'Fire!'),
        ({'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}, 'Shiver me timbers!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert cannons_ready(arg) == expected
