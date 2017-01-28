"""Product of the main diagonal of a square matrix.
https://www.codewars.com/kata/product-of-the-main-diagonal-of-a-square-matrix

Given a list of rows of a square matrix, find the product of the main diagonal.

Examples:

```python
main_diagonal_product([[1,0],[0,1]]) => 1

main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]) => 45
```
```haskell
mainDiagonalProduct []                        `shouldBe` 1          -- matrix: 0x0
mainDiagonalProduct [[1]]                     `shouldBe` 1          -- matrix: 1x1
mainDiagonalProduct [[1,2,3],[4,5,6],[7,8,9]] `shouldBe` 1 * 5 * 9  -- matrix: 3x3
```
```javascript
mainDiagonalProduct([[1,0],[0,1]]) => 1

mainDiagonalProduct([[1,2,3],[4,5,6],[7,8,9]]) => 45
```
```coffeescript
mainDiagonalProduct([[1,0],[0,1]]) => 1

mainDiagonalProduct([[1,2,3],[4,5,6],[7,8,9]]) => 45
```
```ruby
main_diagonal_product([[1,0],[0,1]]) => 1

main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]) => 45
```
```haskell
mainDiagonalProduct []                        `shouldBe` 1          -- matrix: 0x0
mainDiagonalProduct [[1]]                     `shouldBe` 1          -- matrix: 1x1
mainDiagonalProduct [[1,2,3],[4,5,6],[7,8,9]] `shouldBe` 1 * 5 * 9  -- matrix: 3x3
```
http://en.wikipedia.org/wiki/Main_diagonal

"""


from operator import mul
from functools import reduce


def main_diagonal_product(mat):
    return reduce(mul, (mat[i][i] for i in range(len(mat[0]))))
