"""String destroyer (plus extra credit)"""

import pytest

from solutions.kyu_7.string_destroyer_plus_extra_credit import destroyer

EXAMPLES = (
    ('arg', 'expected'),
    [
        (({'A', 'b'}, {'C', 'd'}), "a _ c _ e f g h i j k l m n o p q r s t u v w x y z"),
        (({'b', 'b'}, {'C', 'm', 'f'}), "a _ c d e _ g h i j k l _ n o p q r s t u v w x y z"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert destroyer(arg) == expected
