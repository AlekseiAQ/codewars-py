"""How many e-mails we sent today?"""

import pytest

from solutions.kyu_7.how_many_e_mails_we_sent_today import get_percentage

EXAMPLES = (
    ('sent', 'limit', 'expected'),
    [
        (101, 1000, "10%"),
        (256, 500, "51%"),
        (259, 1000, "25%"),
        (0, 20, "No e-mails sent"),
        (1000, 1000, "Daily limit is reached"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(sent, limit, expected):
    assert get_percentage(sent, limit) == expected
