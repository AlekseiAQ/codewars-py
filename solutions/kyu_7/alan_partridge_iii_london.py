"""Alan Partridge III - London
https://www.codewars.com/kata/alan-partridge-iii-london

<img src="https://static1.squarespace.com/static/553e1e3ae4b0c7db85dc4fb3/5546810be4b0a65de4f4e04a/563f39b3e4b07bcd9d902110/1446984116886/Alan_Partridge_Minimalist_Posteritty_London.jpg?format=1000w">

Ever the learned traveller, Alan Partridge has pretty strong views on London:

```
"Go to London. I guarantee you'll either be mugged or not appreciated.
Catch the train to London, stopping at Rejection, Disappointment, Backstabbing Central and Shattered Dreams Parkway."
```
Your job is to check that the provided list of stations contains all of the stops Alan mentions. There will be other stations in the array.  Example:

```
['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
```

If the stations all appear, return 'Smell my cheese you mother!', if not,  return 'No, seriously, run. You will miss it.'.

Other katas in this series:<br><br>
<a href="https://www.codewars.com/kata/alan-partridge-i-partridge-watch">Alan Partridge I - Partridge Watch</a><br>
<a href="https://www.codewars.com/kata/alan-partridge-ii-apple-turnover">Alan Partridge II - Apple Turnover</a><br>
"""


def alan(arr):
    terms = {'Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway'}
    return "Smell my cheese you mother!" if terms.issubset(arr) else "No, seriously, run. You will miss it."
