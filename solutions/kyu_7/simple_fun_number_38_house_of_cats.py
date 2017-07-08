"""There are some people and cats in a house. You are given the number of legs they have all together. Your task is to return an array containing every possible number of people that could be in the house sorted in ascending order. It's guaranteed that each person has 2 legs and each cat has 4 legs.

Example

For legs = 6, the output should be [1, 3].

There could be either 1 cat and 1 person (4 + 2 = 6) or 3 people (2 * 3 = 6).

For legs = 2, the output should be [1].

There can be only 1 person.

Input/Output

[input] integer legs

The total number of legs in the house.

Constraints: 2 ≤ legs ≤ 100.
[output] an integer array

Every possible number of people that can be in the house.
"""


def house_of_cats(legs):
    return list(range(legs % 4 // 2, legs // 2 + 1, 2))
