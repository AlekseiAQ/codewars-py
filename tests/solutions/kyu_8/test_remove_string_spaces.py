"""Remove String Spaces"""

import pytest

from solutions.kyu_8.remove_string_spaces import no_space

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('8 j 8   mBliB8g  imjB8B8  jl  B', '8j8mBliB8gimjB8B8jlB'),
        ('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd', '88Bifk8hB8BB8BBBB888chl8BhBfd'),
        ('8aaaaa dddd r     ', '8aaaaaddddr'),
        ('jfBm  gk lf8hg  88lbe8 ', 'jfBmgklf8hg88lbe8') ,
        ('8j aam', '8jaam'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert no_space(arg) == expected
