"""Knight vs King
https://www.codewars.com/kata/knight-vs-king

## Knight vs King

If you are not familiar with chess game you can learn more [Here](https://en.wikipedia.org/wiki/Chess) .

Here is the chess board:

![alt text](http://crowd-multilogue.com/Images/Codewars/KataPic5.PNG)

You put a Knight and a king in the board.

Complete the method that tell us which one can capture the other one.
```csharp
public static string KnightVsKing(object[] knightPosition, object[]kingPosition)
        {
        // Three possible outputs are "Knight", "King" and "None".
        }
```
```javascript
function knightVsKing(knightPosition, kingPosition) {
  // Three possible outputs are "Knight", "King" and "None".
}
```
You are provided with two object array; each contains an integer (first item) and a string (second item) to show the position of the pieces in the chess board.

```csharp
object[] kingPosition = {4, "C"};
object[] knightPosition = {6, "D"};
```
```javascript
kingPosition = [4, "C"];
knightPosition = [6, "D"];
```
```python
kingPosition = [4, "C"];
knightPosition = [6, "D"];
```
```ruby
king_position = [4, "C"];
knight_position = [6, "D"];
```

Check the test cases and Happy coding :)

"""


def knightVsKing(knight_position, king_position):
    """ knight_vs_king == PEP8 (forced mixedCase by CodeWars) """
    dx = knight_position[0] - king_position[0]
    dy = ord(knight_position[1]) - ord(king_position[1])
    d = dx * dx + dy * dy
    if d == 5:
        return 'Knight'
    if d < 3:
        return 'King'
    return 'None'
