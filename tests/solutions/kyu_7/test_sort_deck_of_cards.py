"""Sort deck of cards"""

import pytest

from solutions.kyu_7.sort_deck_of_cards import sort_cards

EXAMPLES = (
    ('arg', 'expected'),
    [
        (list('39A5T824Q7J6K'), list('A23456789TJQK')),
        (list('Q286JK395A47T'), list('A23456789TJQK')),
        (list('54TQKJ69327A8'), list('A23456789TJQK')),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_cards(arg) == expected
