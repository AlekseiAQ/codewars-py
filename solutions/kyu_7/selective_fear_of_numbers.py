"""Selective fear of numbers
https://www.codewars.com/kata/selective-fear-of-numbers

I've got a crazy mental illness.
I dislike numbers a lot. But it's a little complicated:
The number I'm feared of depends on which day of week it is...
This a concrete description of my mental illness:

Monday     --> 12

Tuesday    --> numbers greater than 95

Wednesday  --> 34

Thursday   --> 0

Friday     --> numbers divisable by 2

Saturday   --> 56

Sunday     --> 666 or -666


Write a function which takes a string (day of week) and an integer (number to be tested) so it tells the doctor if I'm feared or not. (return a boolean)

"""


def am_I_afraid(day, num):
    return day == "Monday" and num == 12 or\
        day == "Tuesday" and num > 95 or\
        day == "Wednesday" and num == 34 or\
        day == "Thursday" and num == 0 or\
        day == "Friday" and num % 2 == 0 or\
        day == "Saturday" and num == 56 or\
        day == "Sunday" and num in [-666, 666]
