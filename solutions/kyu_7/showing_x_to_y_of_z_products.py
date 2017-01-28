"""Showing X to Y of Z Products.
https://www.codewars.com/kata/showing-x-to-y-of-z-products

A category page displays a set number of products per page, with pagination at the bottom allowing the user to move from page to page.

Given that you know the page you are on, how many products are in the category in total, and how many products are on any given page, how would you output a simple string showing which products you are viewing..

examples

In a category of 30 products with 10 products per page, on page 1 you would see 

'Showing 1 to 10 of 30 Products.'

In a category of 26 products with 10 products per page, on page 3 you would see

'Showing 21 to 26 of 26 Products.'

In a category of 8 products with 10 products per page, on page 1 you would see

'Showing 1 to 8 of 8 Products.'
"""


def pagination_text(page_number, page_size, total_products):
    first = page_size * (page_number - 1) + 1
    last = min(first + page_size - 1, total_products)
    return "Showing %d to %d of %d Products." % (first, last, total_products)
