"""The Lazy Startup Office"""

import pytest

from solutions.kyu_7.the_lazy_startup_office import binRota

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([["Bob","Nora"],["Ruby","Carl"]],["Bob","Nora","Carl","Ruby"]),
        ([["Billy"]],["Billy"]),
        ([["Billy", "Nancy"]],["Billy","Nancy"]),
        ([["Billy"],["Megan"],["Aki"],["Arun"],["Joy"]],["Billy", "Megan", "Aki", "Arun","Joy"]),
        ([["Sam","Nina","Tim","Helen","Gurpreet","Edward","Holly","Eliza"],["Billy","Megan","Aki","Arun","Joy","Anish","Lee","Maryan"],["Nick","Josh","Pete","Kavita","Daisy","Francesca","Alfie","Macy"]],["Sam","Nina","Tim","Helen", "Gurpreet", "Edward", "Holly", "Eliza","Maryan","Lee","Anish","Joy","Arun","Aki","Megan","Billy","Nick","Josh","Pete","Kavita","Daisy","Francesca","Alfie","Macy"]),
        ([["Stefan","Raj","Marie"],["Alexa","Amy","Edward"],["Liz","Claire","Juan"],["Dee","Luke","Elle"]],["Stefan","Raj","Marie","Edward","Amy","Alexa","Liz","Claire","Juan","Elle","Luke","Dee"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert binRota(arg) == expected
