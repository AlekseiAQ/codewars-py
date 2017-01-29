"""Genetic Algorithm Series - #1 Generate
https://www.codewars.com/kata/genetic-algorithm-series-number-1-generate

A genetic algorithm is based in groups of chromosomes, called populations. To start our population of chromosomes we need to generate random binary strings with a specified length.

In this kata you have to implement a function `generate` that receives a `length` and has to return a random binary strign with `length` characters.

![](http://i.imgur.com/XW7Ys4n.gif)

# Example:

Generate a chromosome with length of 4 `generate(4)` could return the chromosome `0010`, `1110`, `1111`... or any of `2^4` possibilities.

***Note:*** *Some tests are random. If you think your algorithm is correct but the result fails, trying again should work.*

# See other katas from this series

  - **Genetic Algorithm Series - #1 Generate**
  - [Genetic Algorithm Series - #2 Mutation](http://www.codewars.com/kata/genetic-algorithm-series-number-2-mutation)
  - [Genetic Algorithm Series - #3 Crossover](http://www.codewars.com/kata/genetic-algorithm-series-number-3-crossover)
  - [Genetic Algorithm Series - #4 Get population and fitnesses](http://www.codewars.com/kata/genetic-algorithm-series-number-4-get-population-and-fitnesses)
  - [Genetic Algorithm Series - #5 Roulette wheel selection](http://www.codewars.com/kata/genetic-algorithm-series-number-5-roulette-wheel-selection)

*This kata is a piece of  ![2 kyu](http://i.imgur.com/CGlQhDW.png) [Binary Genetic Algorithm](http://www.codewars.com/kata/526f35b9c103314662000007)*
"""


import random


def generate(length):
    return ''.join(random.choice('10') for _ in range(length))
