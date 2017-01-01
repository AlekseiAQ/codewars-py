"""How good are you really?
https://www.codewars.com/kata/how-good-are-you-really

There was a test in your class and you passed it. Congratulations!</br>
But you're an ambitious person. You want to know if you're better than the average student in your class.</br>
You got an array with your colleges' points. Now calculate the average to your points!</br>

Return `True` if you're better, else `False`!

### Note:

Your points are not included in the array of your classes points. For calculating the average point you may add your point to the given array!
"""


def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
