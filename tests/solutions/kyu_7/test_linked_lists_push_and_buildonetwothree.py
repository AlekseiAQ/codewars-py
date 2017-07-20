"""Linked Lists - Push & BuildOneTwoThree"""

import pytest
from solutions.kyu_7.linked_lists_push_and_buildonetwothree import \
    Node, build_one_two_three, push

EXAMPLES = (
    ('arg', 'expected'),
    [
        (push(None, 1).data, 1,),
        (push(None, 1).next, None,),
        (push(Node(1), 2).data, 2,),
        (push(Node(1), 2).next.data, 1,),
        (build_one_two_three().data, 1,),
        (build_one_two_three().next.data, 2,),
        (build_one_two_three().next.next.data, 3,),
        (build_one_two_three().next.next.next, None,),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
