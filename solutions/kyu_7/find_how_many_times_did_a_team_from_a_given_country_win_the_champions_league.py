"""Find how many times did a team from a given country win the Champions League?
https://www.codewars.com/kata/find-how-many-times-did-a-team-from-a-given-country-win-the-champions-league

Create a function that takes two arguments:

1) An array of objects which feature the season, the team and the country of the Champions League winner.

2) Country (as a string, for example, 'Portugal')

You function should then return the number which represents the number of times a team from a given country has won. Return `0` if there have been no wins.

For example if the input array is as follows:

<img src=http://i.imgur.com/61bIUDY.png>


`countWins(winnerList1, 'Spain')` => should return 2<br>
`countWins(winnerList1, 'Portugal')` => should return 1<br>
`countWins(winnerList1, 'Sportland')` => should return 0<br>


"""


def countWins(winnerList, country):
    """ count_wins, winner_list == PEP8 (forced mixedCase by CodeWars) """
    return sum(el['country'] == country for el in winnerList)
