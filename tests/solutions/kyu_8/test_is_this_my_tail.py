"""Is this my tail?"""

import pytest

from solutions.kyu_8.is_this_my_tail import correct_tail

EXAMPLES = (
    ('args', 'expected'),
    [
        (("Fox", "x"), True),
        (("Rhino", "o"), True),
        (("Meerkat", "t"), True),
        (("Emu", "t"), False),
        (("Badger", "s"), False),
        (("Giraffe", "d"), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert correct_tail(*args) == expected
