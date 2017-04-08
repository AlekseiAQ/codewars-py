"""Managing Homework Time
https://www.codewars.com/kata/managing-homework-time

**The scenario:** You have to complete a textbook assignment full of boring math problems as homework due in 5 days time. You want to find out how long you must spend on each of the 5 days to evenly spread the workload.

You will create a program, ```time_per_day```, that will take a list of tuples. Each tuple represents a section of the assignment and contains **two integer values**. The first value represents the complexity of each question and the second value represents the number of questions.

On average, you take:

* 0.75 minutes to complete a question of complexity value 1;
* 1.5 minutes to complete a question of complexity 2;
* 2.25 minutes to complete a question of complexity 3; 

...and so on. You must return the amount of time to spend for each of the 5 days in **hours**, rounded to **2 decimal points**.

**Example:** If the parameter passed is ```[(1, 20), (2, 10), (3, 15), (4, 10)]```, the funtion should return 0.31 (If you are unsure about how to go about the solution, try working the example out on paper first before attempting to recreate it.)

**Try refining your code by writing it in one line.**
"""


def time_per_day(l):
    return round(sum(0.75 * c * n for (c, n) in l) / 300, 2)
