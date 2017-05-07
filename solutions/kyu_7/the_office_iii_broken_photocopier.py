"""The Office III - Broken Photocopier
https://www.codewars.com/kata/the-office-iii-broken-photocopier

The bloody photocopier is broken... Just as you were sneaking around the office to print off your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.

<a href='https://www.codewars.com/kata/the-office-i-outed'>The Office I - Outed</a><br>
<a href='https://www.codewars.com/kata/the-office-ii-boredom-score'>The Office II - Boredeom Score</a><br>
<a href='https://www.codewars.com/kata/the-office-iv-find-a-meeting-room'>The Office IV - Find a Meeting Room</a><br>
<a href='https://www.codewars.com/kata/the-office-v-find-a-chair'>The Office V - Find a Chair</a><br>



"""


def broken(inp):
    return inp.translate(str.maketrans('01', '10'))
