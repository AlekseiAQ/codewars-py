"""Cat and Mouse - Easy Version
https://www.codewars.com/kata/cat-and-mouse-easy-version

You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'. 

You need to find out if the cat can catch the mouse from it's current position. The cat can jump three characters. So:

C.....m returns 'Escaped!'  <-- more than three characters between

C...m returns 'Caught!'   <-- as there are three characters between the two, the cat can jump.
"""


def cat_mouse(x):
    if x.index("C") - x.index("m") > 4 or x.index("m") - x.index("C") > 4:
        return "Escaped!"
    else:
        return "Caught!"
