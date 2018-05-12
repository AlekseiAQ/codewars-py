"""Professor Oak's Trouble - New Pokedex prototype"""

import pytest

from solutions.kyu_7.professor_oaks_trouble_new_pokedex_prototype import \
    PokeScan

EXAMPLES = (
    ('arg', 'expected'),
    [
        (PokeScan('Squirtle', 0, 'water').info(),
        'Squirtle, a wet and weak Pokemon.'),
        (PokeScan('Charmander', 0, 'fire').info(),
        'Charmander, a fiery and weak Pokemon.'),
        (PokeScan('Bulbasaur', 0, 'grass').info(),
        'Bulbasaur, a grassy and weak Pokemon.'),
        (PokeScan('Squirtle', 20, 'water').info(),
        'Squirtle, a wet and weak Pokemon.'),
        (PokeScan('Charmander', 20, 'fire').info(),
        'Charmander, a fiery and weak Pokemon.'),
        (PokeScan('Bulbasaur', 20, 'grass').info(),
        'Bulbasaur, a grassy and weak Pokemon.'),
        (PokeScan('Squirtle', 21, 'water').info(),
        'Squirtle, a wet and fair Pokemon.'),
        (PokeScan('Charmander', 21, 'fire').info(),
        'Charmander, a fiery and fair Pokemon.'),
        (PokeScan('Bulbasaur', 21, 'grass').info(),
        'Bulbasaur, a grassy and fair Pokemon.'),
        (PokeScan('Squirtle', 50, 'water').info(),
        'Squirtle, a wet and fair Pokemon.'),
        (PokeScan('Charmander', 50, 'fire').info(),
        'Charmander, a fiery and fair Pokemon.'),
        (PokeScan('Bulbasaur', 50, 'grass').info(),
        'Bulbasaur, a grassy and fair Pokemon.'),
        (PokeScan('Squirtle', 51, 'water').info(),
        'Squirtle, a wet and strong Pokemon.'),
        (PokeScan('Charmander', 51, 'fire').info(),
        'Charmander, a fiery and strong Pokemon.'),
        (PokeScan('Bulbasaur', 51, 'grass').info(), 
        'Bulbasaur, a grassy and strong Pokemon.'),
        (PokeScan('Squirtle', 100, 'water').info(),
        'Squirtle, a wet and strong Pokemon.'),
        (PokeScan('Charmander', 100, 'fire').info(),
        'Charmander, a fiery and strong Pokemon.'),
        (PokeScan('Bulbasaur', 100, 'grass').info(),
         'Bulbasaur, a grassy and strong Pokemon.'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
