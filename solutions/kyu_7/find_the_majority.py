"""Find the majority
https://www.codewars.com/kata/find-the-majority

<h3>Goal</h3>
Given a list of elements [a1, a2, ..., an], with each <i>ai</i> being a string, write a function **majority** that returns the value that appears the most in the list.

If there's no winner, the function should return None, NULL, nil, etc, based on the programming language.

<h3>Example</h3>
majority(["A", "B", "A"]) returns "A"
majority(["A", "B", "B", "A"]) returns None
"""


from collections import Counter


def majority(arr):
    items = Counter(arr).most_common(2)
    return (
        None
        if (not arr or (len(items) == 2 and items[0][1] == items[1][1]))
        else items[0][0]
    )
