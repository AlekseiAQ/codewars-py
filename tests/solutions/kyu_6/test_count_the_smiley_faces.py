"""Count the smiley faces!"""

import pytest

from solutions.kyu_6.count_the_smiley_faces import count_smileys

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([], 0),
        ([':D',':~)',';~D',':)'], 4),
        ([':)',':(',':D',':O',':;'], 2),
        ([';]', ':[', ';*', ':$', ';-D'], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert count_smileys(arg) == expected
