"""The Office IV - Find a Meeting Room
https://www.codewars.com/kata/the-office-iv-find-a-meeting-room

Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly wants to have a meeting with you, and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the **first** empty one and return it's index (N.B. There may be more than one empty room in some test cases). 

'X' --> busy
'O' --> empty

If all rooms are busy, return 'None available!'.


More in this series:

<a href='https://www.codewars.com/kata/the-office-i-outed'>The Office I - Outed</a><br>
<a href='https://www.codewars.com/kata/the-office-ii-boredom-score'>The Office II - Boredeom Score</a><br>
<a href='https://www.codewars.com/kata/the-office-iii-broken-photocopier'>The Office III - Broken Photocopier</a><br>
<a href='https://www.codewars.com/kata/the-office-v-find-a-chair'>The Office V - Find a Chair</a><br>

"""


def meeting(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return 'None available!'
