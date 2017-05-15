"""Histogram - H1"""

import pytest

from solutions.kyu_7.histogram_h1 import histogram

res = """6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
"""

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([7,3,10,1,0,5], res),
        ([0,0,0,0,0,0], "6|\n5|\n4|\n3|\n2|\n1|\n"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert histogram(arg) == expected
