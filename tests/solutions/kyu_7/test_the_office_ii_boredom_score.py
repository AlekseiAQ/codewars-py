"""The Office II - Boredom Score"""

import pytest

from solutions.kyu_7.the_office_ii_boredom_score import boredom

EXAMPLES = (
    ('arg', 'expected'),
    [
        ({"tim": "change", "jim": "accounts", "randy": "canteen",
          "sandy": "change", "andy": "change", "katie": "IS",
          "laura": "change", "saajid": "IS", "alex": "trading",
          "john": "accounts", "mr": "finance"},
          "kill me now"),
        ({"tim": "IS", "jim": "finance", "randy": "pissing about",
          "sandy": "cleaning", "andy": "cleaning", "katie": "cleaning",
          "laura": "pissing about", "saajid": "regulation",
          "alex": "regulation", "john": "accounts", "mr": "canteen"},
          "i can handle this"),
        ({"tim": "accounts", "jim": "accounts", "randy": "pissing about",
          "sandy": "finance", "andy": "change", "katie": "IS", "laura": "IS",
          "saajid": "canteen", "alex": "pissing about", "john": "retail",
          "mr": "pissing about"},
          "party time!!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert boredom(arg) == expected
