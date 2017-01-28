"""Complete The Pattern #2
https://www.codewars.com/kata/complete-the-pattern-number-2

<p style="text-align:left;"><font face="Impact" size="5"><A HREF="http://www.codewars.com/kata/complete-the-pattern-number-1">< PREVIOUS KATA</A></font>
 <span style="float:right;"><font face="Impact" size="5" ><A HREF="http://www.codewars.com/kata/557341907fbf439911000022">NEXT KATA ></A></font></span></p>
 
 
 ###Task:
You have to write a function `pattern` which returns the following Pattern(See Pattern & Examples) upto `n` number of rows. 

* Note:`Returning` the pattern is not the same as `Printing` the pattern.

####Rules/Note:
* If `n < 1` then it should return "" i.e. empty string.
* There are `no whitespaces` in the pattern.

###Pattern:

    (n)(n-1)(n-2)...4321
    (n)(n-1)(n-2)...432
    (n)(n-1)(n-2)...43
    (n)(n-1)(n-2)...4
    ...............
    ..............
    (n)(n-1)(n-2)
    (n)(n-1)
    (n)
    
###Examples:

* pattern(4):

      4321
      432
      43
      4
    
* pattern(11):

      1110987654321
      111098765432
      11109876543
      1110987654
      111098765
      11109876
      1110987
      111098
      11109
      1110
      11


```Hint: Use \n in string to jump to next line```

<P ALIGN="center"><FONT FACE="Impact"  SIZE="5"><A HREF="http://www.codewars.com/users/curious_db97/authored">>>>LIST OF ALL MY KATAS<<<</A></FONT></P>
"""


def pattern(n):
    return '\n'.join(''.join(map(str, range(n, i-1, -1))) for i in range(1, n+1))
