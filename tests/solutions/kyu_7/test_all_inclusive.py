"""All Inclusive?"""

import pytest

from solutions.kyu_7.all_inclusive import contain_all_rots

EXAMPLES = (
    ('args', 'expected'),
    [
        (("", []), True),
        (("", ["bsjq", "qbsj"]), True),
        (("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True),
        (("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert contain_all_rots(*args) == expected
