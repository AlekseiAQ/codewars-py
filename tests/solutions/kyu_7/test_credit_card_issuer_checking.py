"""Credit card issuer checking"""

import pytest

from solutions.kyu_7.credit_card_issuer_checking import get_issuer

EXAMPLES = (
    ('arg', 'expected'),
    [
        (4111111111111111, 'VISA'),
        (378282246310005, 'AMEX'),
        (9111111111111111, 'Unknown'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_issuer(arg) == expected
