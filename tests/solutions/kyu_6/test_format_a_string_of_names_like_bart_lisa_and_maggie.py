"""Format a string of names like 'Bart, Lisa & Maggie'."""

import pytest

from solutions.kyu_6.format_a_string_of_names_like_bart_lisa_and_maggie import namelist

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}], 'Bart, Lisa, Maggie, Homer & Marge'),
        ([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}], 'Bart, Lisa & Maggie'),
        ([{'name': 'Bart'},{'name': 'Lisa'}], 'Bart & Lisa'),
        ([{'name': 'Bart'}], 'Bart'),
        ([], ''),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert namelist(arg) == expected
