"""Sum of array singles
https://www.codewars.com/kata/sum-of-array-singles

In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, `repeats([4,5,7,5,4,8]) = 15` because only the numbers `7` and `8` occur once, and their sum is `15`.

More examples in the test cases.

<!-- C# documentation -->
```if:csharp
<h1>Documentation:</h1>
<h2>Kata.Repeats Method (List&lt;Int32&gt;)</h2>

Takes a list where all ints are repeated twice, except two ints, and returns the sum of the ints of a list where those ints only occur once.

<span style="font-size:20px">Syntax</span>
<div style="margin-top:-10px;padding:2px;background-color:Grey;position:relative;left:20px;width:600px;">
  <div style="background-color:White;color:Black;border:1px;display:block;padding:10px;padding-left:18px;font-family:Consolas,Courier,monospace;">
    <span style="color:Blue;">public</span>
    <span style="color:Blue;">static</span>
    <span style="color:Blue;">int</span> Repeats(</br>
    <span style="position:relative;left:62px;">List&lt;<span style="color:Blue;">int</span>&gt; source</span></br>
  ��)
  </div>
</div>
</br>
<div style="position:relative;left:20px;">
  <strong>Parameters</strong>
  </br>
  <i>source</i>
  </br>
  <span style="position:relative;left:50px;">Type: <a href="https://msdn.microsoft.com/en-us/library/6sh2ey19(v=vs.110).aspx">System.Collections.Generic.List</a>&lt;Int32&gt;</span></br>
  <span style="position:relative;left:50px;">The list to process.</span>
  </br></br>
  <strong>Return Value</strong>
  </br>
  <span>Type: <a href="https://msdn.microsoft.com/en-us/library/system.int32(v=vs.110).aspx">System.Int32</a></span></br>
  The sum of the elements of the list where those elements have no duplicates.
</div>
```
<!-- end C# documentation -->

Good luck!

If you like this Kata, please try:

[Sum of prime-indexed elements](https://www.codewars.com/kata/59f38b033640ce9fc700015b)

[Sum of integer combinations](https://www.codewars.com/kata/59f3178e3640cef6d90000d5)
"""


from collections import Counter

def repeats(arr):
    counter = Counter(arr)
    return sum(el for el in counter.elements() if counter[el] == 1)
