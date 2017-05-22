"""Alan Partridge III - London"""

import pytest

from solutions.kyu_7.alan_partridge_iii_london import alan

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["Norwich", "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway", "London"], "Smell my cheese you mother!"),
        (["London", "Norwich"], "No, seriously, run. You will miss it."),
        (["Norwich", "Tooting", "Bank", "Rejection", "Disappointment", "Backstabbing Central", "Exeter", "Shattered Dreams Parkway", "Belgium","London"], "Smell my cheese you mother!"),
        (["London", "Norwich"], "No, seriously, run. You will miss it."),
        (["London", "Shattered Dreams Parkway", "Backstabbing Central", "Disappointment", "Rejection", "Norwich"], "Smell my cheese you mother!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert alan(arg) == expected
