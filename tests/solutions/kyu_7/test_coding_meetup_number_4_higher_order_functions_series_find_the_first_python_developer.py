"""Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer"""

import pytest

from solutions.kyu_7.coding_meetup_number_4_higher_order_functions_series_find_the_first_python_developer import get_first_python

list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]

list2 = [
  { "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
  { "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
]

list3 = [
  { "first_name": "Sofia", "last_name": "P.", "country": "Italy", "continent": "Europe", "age": 41, "language": "Clojure" },
  { "first_name": "Jayden", "last_name": "P.", "country": "Jamaica", "continent": "Americas", "age": 42, "language": "JavaScript" },
  { "first_name": "Sou", "last_name": "B.", "country": "Japan", "continent": "Asia", "age": 43, "language": "Python" },
  { "first_name": "Rimas", "last_name": "C.", "country": "Jordan", "continent": "Asia", "age": 44, "language": "Java" }
]

EXAMPLES = (
    ('arg', 'expected'),
    [
        (list1, "Victoria, Puerto Rico"),
        (list2, "There will be no Python developers"),
        (list3, "Sou, Japan"),
        (list1+list3, "Victoria, Puerto Rico"),
        (list3+list1, "Sou, Japan"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_first_python(arg) == expected
