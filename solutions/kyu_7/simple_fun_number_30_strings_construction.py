"""How many strings equal to A can be constructed using letters from the string B? Each letter can be used only once and in one string only.

Example

For A = "abc" and B = "abccba", the output should be 2.

We can construct 2 strings A with letters from B.

Input/Output

[input] string A

String to construct, A contains only lowercase English letters.

Constraints: 3 ≤ A.length ≤ 9.
[input] string B

String containing needed letters, B contains only lowercase English letters.

Constraints: 3 ≤ B.length ≤ 50.
[output] an integer
"""


from collections import Counter


def strings_construction(a, b):
    ca, cb = Counter(a), Counter(b)
    return min(cb.get(char, 0) // count for char, count in ca.items())
