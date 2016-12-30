"""Rock Paper Scissors!
https://www.codewars.com/kata/rock-paper-scissors

# Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return `Draw!`.

Examples:

```js
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
```

![rockpaperscissors](http://i.imgur.com/aimOQVX.png)
"""


def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return 'Player 1 won!'
    if beats[p2] == p1:
        return 'Player 2 won!'
    return 'Draw!'
