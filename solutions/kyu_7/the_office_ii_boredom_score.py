"""The Office II - Boredom Score
https://www.codewars.com/kata/the-office-ii-boredom-score

Every now and then people in the office moves teams or departments. Depending what people are doing with their time they can become more or less boring. Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.

Each department has a different boredom assessment score, as follows:

accounts = 1<br>
finance = 2 <br>
canteen = 10 <br>
regulation = 3 <br>
trading = 6 <br>
change = 6<br>
IS = 8<br>
retail = 5<br> 
cleaning = 4<br>
pissing about = 25<br>

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'<br>
< 100 & > 80: 'i can handle this'<br>
100 or over: 'party time!!'

<a href='https://www.codewars.com/kata/the-office-i-outed'>The Office I - Outed</a><br>
<a href='https://www.codewars.com/kata/the-office-iii-broken-photocopier'>The Office III - Broken Photocopier</a><br>
<a href='https://www.codewars.com/kata/the-office-iv-find-a-meeting-room'>The Office IV - Find a Meeting Room</a><br>
<a href='https://www.codewars.com/kata/the-office-v-find-a-chair'>The Office V - Find a Chair</a><br>
"""


def boredom(staff):
    SCORE = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,
    }
    s = sum(SCORE.get(dep) for dep in staff.values())
    if s <= 80:
        return 'kill me now'
    elif 80 < s < 100:
        return 'i can handle this'
    elif s > 100:
        return 'party time!!'
