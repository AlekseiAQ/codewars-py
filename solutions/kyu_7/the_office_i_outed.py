"""The Office I - Outed
https://www.codewars.com/kata/the-office-i-outed

Your colleagues have been looking over you shoulder. When you should have been doing your boring real job, you've been using the work computers to smash in endless hours of codewars.

In a team meeting, a terrible, awful person declares to the group that you aren't working. You're in trouble. You quickly have to gauge the feeling in the room to decide whether or not you should gather your things and leave. 

Given an object (meet) containing team member names as keys, and their happiness rating out of 10 as the value, you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.

Happiness rating will be total score / number of people in the room.

Note that your boss is in the room (boss), their score is worth double it's face value (but they are still just one person!).

<a href='https://www.codewars.com/kata/the-office-ii-boredom-score'>The Office II - Boredom Score</a><br>
<a href='https://www.codewars.com/kata/the-office-iii-broken-photocopier'>The Office III - Broken Photocopier</a><br>
<a href='https://www.codewars.com/kata/the-office-iv-find-a-meeting-room'>The Office IV - Find a Meeting Room</a><br>
<a href='https://www.codewars.com/kata/the-office-v-find-a-chair'>The Office V - Find a Chair</a><br>
"""


def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet.get(boss)) / len(meet) <= 5 else 'Nice Work Champ!'
