"""What is my name score? #1"""

import pytest

from solutions.kyu_7.what_is_my_name_score_number_1 import name_score

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Mary Jane', {"Mary Jane":20}),
        ('Luke Skywalker', {"Luke Skywalker":41}),
        ('Zoe Andrews', {"Zoe Andrews":23}),
        ('Double  Space', {"Double  Space":25}),
        ('Greg Z MacDonald', {"Greg Z MacDonald":26}),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert name_score(arg) == expected
