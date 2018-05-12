"""Professor Oak's Trouble - New Pokedex prototype
https://www.codewars.com/kata/professor-oaks-trouble-new-pokedex-prototype

Professor Oak has just begun learning Python and he wants to program his new Pokedex prototype with it.

For a starting point, he wants to instantiate each scanned Pokemon as an object that is stored at Pokedex's memory. He needs your help!

Your task is to:

1) Create a ```PokeScan``` class that takes in 3 arguments: ```name```, ```level``` and ```pkmntype```.

2) Create a ```info``` method for this class that returns some comments about the Pokemon, specifying it's name, an observation about the ```pkmntype``` and other about the ```level```.

3) Keep in mind that he has in his possession just three Pokemons for you to test the scanning function: ```Squirtle```, ```Charmander``` and ```Bulbasaur```, of ```pkmntypes``` ```water```, ```fire``` and ```grass```, respectively.

4) The ```info``` method shall return a string like this:
```Charmander, a fiery and strong Pokemon.```

5) If the Pokemon level is less than or equal to 20, it's a ```weak``` Pokemon. If greater than 20 and less than or equal to 50, it's a ```fair``` one. If greater than 50, it's a ```strong``` Pokemon.

6) For the ```pkmntypes```, the observations are ```wet```, ```fiery``` and ```grassy``` Pokemon, according to each Pokemon type.

IMPORTANT: The correct spelling of "Pok�mon" is "Pok�mon", with the ```"�"```, but to maximize the compatibility of the code I've had to write it as ```"Pokemon"```, without the ```"�"```. So, in your code, don't use  the ```"�"```.
"""


class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    @property
    def element(self):
        return {
            'water': 'wet',
            'fire': 'fiery',
            'grass': 'grassy'
        }.get(self.pkmntype)

    @property
    def strength(self):
        return 'strong' if self.level > 50 else \
            'fair' if self.level > 20 else \
            'weak'

    def info(self):
        return '{}, a {} and {} Pokemon.'.format(
            self.name, self.element, self.strength)
