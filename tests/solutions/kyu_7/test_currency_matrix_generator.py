"""Currency Matrix Generator"""

import pytest

from solutions.kyu_7.currency_matrix_generator import generate_currency_matrix

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('EUR',
         ['EURGBP', 'EURAUD', 'EURNZD', 'EURUSD', 'EURCAD', 'EURCHF',
          'EURJPY']),
        ('GBP',
         ['EURGBP', 'GBPAUD', 'GBPNZD', 'GBPUSD', 'GBPCAD', 'GBPCHF',
          'GBPJPY']),
        ('AUD',
         ['EURAUD', 'GBPAUD', 'AUDNZD', 'AUDUSD', 'AUDCAD', 'AUDCHF',
          'AUDJPY']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert generate_currency_matrix(arg) == expected
