"""Product of the main diagonal of a square matrix."""

import pytest

from solutions.kyu_7.product_of_the_main_diagonal_of_a_square_matrix import main_diagonal_product

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([[1,0],[0,1]], 1),
        ([[1,2,3],[4,5,6],[7,8,9]], 45),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert main_diagonal_product(arg) == expected
