"""Showing X to Y of Z Products."""

import pytest

from solutions.kyu_7.showing_x_to_y_of_z_products import pagination_text

EXAMPLES = (
    ('page_number', 'page_size', 'total_products', 'expected'),
    [
        (1,10,30,"Showing 1 to 10 of 30 Products."),
        (3,10,26,"Showing 21 to 26 of 26 Products."),
        (1,10,8,"Showing 1 to 8 of 8 Products."),
        (2,30,350,"Showing 31 to 60 of 350 Products."),
        (1,23,30,"Showing 1 to 23 of 30 Products."),
        (2,23,30,"Showing 24 to 30 of 30 Products."),
        (43,15,3456,"Showing 631 to 645 of 3456 Products."),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(page_number, page_size, total_products, expected):
    assert pagination_text(page_number, page_size, total_products) == expected
