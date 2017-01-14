"""Get Planet Name By ID
https://www.codewars.com/kata/get-planet-name-by-id

The function is not returning the correct values. Can you figure out why?

```javascript
getPlanetName(3); // should return 'Earth'
```
```ruby
get_planet_name(3) # should return 'Earth'
```
```ruby
get_planet_name(3) # should return 'Earth'
```
```coffeescript
getPlanetName(3) # should return 'Earth'
```

"""


def get_planet_name(id_):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id_, None)
