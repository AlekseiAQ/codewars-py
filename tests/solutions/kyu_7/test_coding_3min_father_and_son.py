"""Coding 3min: Father and Son"""

import pytest

from solutions.kyu_7.coding_3min_father_and_son import sc

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Aab", "Aa"),
        ("AabBc", "AabB"),
        ("SONson", "SONson"),
        ("FfAaTtHhEeRr", "FfAaTtHhEeRr"),
        ("SONsonfather", "SONson"),
        ("sonfather", ""),
        ("DONKEYmonkey", "ONKEYonkey"),
        ("monkeyDONKEY", "onkeyONKEY"),
        ("BANAna", "ANAna"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sc(arg) == expected
