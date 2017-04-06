"""They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?"""

import pytest

from solutions.kyu_8.they_say_that_only_the_name_is_long_enough_to_attract_attention_they_also_said_that_only_a_simple_kata_will_have_someone_to_solve_it_this_is_a_sadly_story_number_1_are_they_opposite import is_opposite

EXAMPLES = (
    ('s1', 's2', 'expected'),
    [
        ("ab","AB", True),
        ("aB","Ab", True),
        ("aBcd","AbCD", True),
        ("AB","Ab", False),
        ("","", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(s1, s2, expected):
    assert is_opposite(s1, s2) == expected
