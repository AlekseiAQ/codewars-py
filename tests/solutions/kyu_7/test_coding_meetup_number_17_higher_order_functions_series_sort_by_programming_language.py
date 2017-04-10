"""Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language"""

import pytest

from solutions.kyu_7.coding_meetup_number_17_higher_order_functions_series_sort_by_programming_language import sort_by_language

arr1 = [
  {"first_name": "Kseniya", "last_name": "A.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
  {"first_name": "Jing", "last_name": "X.", "country": "China", "continent": "Asia", "age": 39, "language": "Ruby" },
  {"first_name": "Andrei", "last_name": "E.", "country": "Romania", "continent": "Europe", "age": 59, "language": "C" },
  {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 60, "language": "C" },
  {"first_name": "Chloe", "last_name": "K.", "country": "Guernsey", "continent": "Europe", "age": 88, "language": "Ruby" },
  {"first_name": "Viktoria", "last_name": "W.", "country": "Bulgaria", "continent": "Europe", "age": 98, "language": "PHP" },
  {"first_name": "Piotr", "last_name": "B.", "country": "Poland", "continent": "Europe", "age": 128, "language": "JavaScript" }
]

arr2 = [
  {"first_name": "Paulo", "last_name": "K.", "country": "Brazil", "continent": "Americas", "age": 19, "language": "Python" }
]

arr3 = [  
  {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
  {"first_name": "Precious", "last_name": "G.", "country": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript" },
  {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
]

arr4 = [  
  {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby" },
  {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C" },
  {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript" }
]

arr5 = arr4 + arr3 

EXAMPLES = (
    ('arg', 'expected'),
    [
        (arr1, [{"first_name": "Andrei", "last_name": "E.", "country": "Romania", "continent": "Europe", "age": 59, "language": "C"}, {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 60, "language": "C"}, {"first_name": "Kseniya", "last_name": "A.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript"}, {"first_name": "Piotr", "last_name": "B.", "country": "Poland", "continent": "Europe", "age": 128, "language": "JavaScript"}, {"first_name": "Viktoria", "last_name": "W.", "country": "Bulgaria", "continent": "Europe", "age": 98, "language": "PHP"}, {"first_name": "Chloe", "last_name": "K.", "country": "Guernsey", "continent": "Europe", "age": 88, "language": "Ruby"}, {"first_name": "Jing", "last_name": "X.", "country": "China", "continent": "Asia", "age": 39, "language": "Ruby"}]),
        (arr2, [{"first_name": "Paulo", "last_name": "K.", "country": "Brazil", "continent": "Americas", "age": 19, "language": "Python"}]),
        (arr3, [{"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C"}, {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript"}, {"first_name": "Precious", "last_name": "G.", "country": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript"}, {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby"}]),
        (arr4, [{"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C"}, {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript"}, {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby"}]),
        (arr5, [{"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C"}, {"first_name": "Maria", "last_name": "S.", "country": "Peru", "continent": "Americas", "age": 30, "language": "C"}, {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript"}, {"first_name": "Agustin", "last_name": "V.", "country": "Uruguay", "continent": "Americas", "age": 19, "language": "JavaScript"}, {"first_name": "Precious", "last_name": "G.", "country": "South Africa", "continent": "Africa", "age": 22, "language": "JavaScript"}, {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby"}, {"first_name": "Nikau", "last_name": "R.", "country": "New Zealand", "continent": "Oceania", "age": 39, "language": "Ruby"}]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_by_language(arg) == expected
