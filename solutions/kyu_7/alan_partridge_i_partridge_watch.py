"""Alan Partridge I - Partridge Watch
https://www.codewars.com/kata/alan-partridge-i-partridge-watch

<img src="https://images-eu.ssl-images-amazon.com/images/I/61FUCzdEinL._AA300_.jpg" align="middle"><br><br>
To celebrate today's launch of my Hero's new book: Alan Partridge: Nomad, We have a new series of kata arranged around the great man himself.

Given an array of terms, if any of those terms relate to Alan Partridge, return Mine's a Pint!

The number of ! after the t should be determined by the number of Alan related terms you find in the provided array (x). The related terms are:

Partridge<br>
PearTree<br>
Chat<br>
Dan<br>
Toblerone<br>
Lynn<br>
AlphaPapa<br>
Nomad<br>

If you don't find any related terms, return 'Lynn, I've pierced my foot on a spike!!'

All Hail King Partridge

Other katas in this series:<br><br>
<a href="https://www.codewars.com/kata/alan-partridge-ii-apple-turnover">Alan Partridge II - Apple Turnover</a><br>
<a href=" https://www.codewars.com/kata/alan-partridge-iii-london
">Alan Partridge III - London</a><br>
"""


def part(arr):
    terms = ["Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]
    s = sum(a in terms for a in arr)
    if s > 0:
        return "Mine's a Pint!" + "!" * (s - 1)
    else:
        return "Lynn, I've pierced my foot on a spike!!"
