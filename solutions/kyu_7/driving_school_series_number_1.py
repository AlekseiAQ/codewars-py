"""Driving School Series #1 
https://www.codewars.com/kata/driving-school-series-number-1

Every month, a random number of students take the driving test at Fast & Furious(F&F) Driving School. To pass the test, a student cannot accumulate more than 18 demerit points. 

At the end of the month, F&F wants to calculate the average demerit points accumulated by <b>ONLY</b> the students who have passed,rounded to the nearest integer. 

Write a function which would allow them to do so. If no students passed the test that month, return 'No pass scores registered.'.
<br></br>

<u>Example:</u>

[10,10,10,18,20,20] --> 12


<u>Note:</u>

The maximum number of demerit points a student can score before the tester calls it a day is 40. 




"""


from numpy import mean


def passed(list_):
    list_ = list(filter(lambda x: x <= 18, list_))
    return round(mean(list_)) if list_ else 'No pass scores registered.'
