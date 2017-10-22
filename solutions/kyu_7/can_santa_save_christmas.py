"""Can Santa save Christmas?
https://www.codewars.com/kata/can-santa-save-christmas

<h2><b>Can Santa save Christmas?</b></h2>
Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.
<br>
But he has only 24 hours left. Can he do it?

Your job is to determine if Santa can distribute all the presents in 24 hours.
<br>
<h3>Your Task:</h3>

You will get an array as input with time durations as string in the following format: <br>
<code>"hh:mm:ss"</code><br>
<br>
<b>Each duration is a present Santa has to distribute.</b>
<br><br>
Return <code>true</code> or <code>false</code> whether he can do it in 24 hours or not.
<br>
<br>
If this kata was to easy for you. Try the <a href="https://www.codewars.com/kata/christmas-present-calculator">harder one.</a>
<br>
<br>
<b>This kata is part of the Collection "Date fundamentals":</b>
<ul>
<li><a href="https://www.codewars.com/kata/count-the-days/javascript">#1 Count the Days!</a></li>
<li><a href="https://www.codewars.com/kata/minutes-to-midnight">#2 Minutes to Midnight</a></li>
<li>#3 Can Santa save Christmas?</li>
<li><a href="https://www.codewars.com/kata/christmas-present-calculator">#4 Christmas Present Calculator</a></li>
</ul>
"""


def determineTime(arr):
    """ determine_time == PEP8 (forced mixedCase by CodeWars) """
    total_sec = sum(h * 3600 + m * 60 + s for
                    h, m, s in [list(map(int, elem.split(':'))) for
                                elem in arr])
    return total_sec < 86400
