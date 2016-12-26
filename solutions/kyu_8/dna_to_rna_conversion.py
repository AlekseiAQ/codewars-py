"""DNA to RNA Conversion
https://www.codewars.com/kata/dna-to-rna-conversion

Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a funciton which translates a given DNA string into RNA.

For example:
```python
DNAtoRNA("GCAT") returns ("GCAU")
```
```ruby
DNAtoRNA("GCAT") returns ("GCAU")
```
```javascript
DNAtoRNA("GCAT") returns ("GCAU")
```
```coffeescript
DNAtoRNA "GCAT" returns "GCAU"
```
```elixir
dna_to_rna("GCAT") #=> "GCAU"
```
```haskell
dnaToRna "GCAT" returns "GCAU"
```
```java
new Bio().dnaToRna("GCAT") // returns "GCAU"
```
```rust
dna_to_rna("GCAT") //=> "GCAU"
```

"""

#function name from task
def DNAtoRNA(dna):
    return dna.translate(str.maketrans('T', 'U'))
