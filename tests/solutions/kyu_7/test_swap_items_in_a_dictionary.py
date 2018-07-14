"""Swap items in a dictionary"""

import pytest

from solutions.kyu_7.swap_items_in_a_dictionary import switch_dict

dict_ = {
    'Ice': 'Cream',
    'Age': '21',
    'Light': 'Cream',
    'Double': 'Cream'
}

expected_dict = {
    'Cream': ['Ice', 'Double', 'Light'],
    '21': ['Age']
}

EXAMPLES = (
    ('arg', 'expected'),
    [
        (dict_, expected_dict),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    user_dict = switch_dict(arg)
    user_dict = {k: sorted(user_dict[k]) for k in user_dict}
    expected_dict = {k: sorted(expected[k]) for k in expected}
    assert user_dict == expected_dict
