"""Complete The  Pattern #1 
https://www.codewars.com/kata/complete-the-pattern-number-1

<p style="text-align:right;"><font face="Impact" size="5"><A HREF="http://www.codewars.com/kata/55733d3ef7c43f8b0700007c">NEXT KATA ></A></font>

 
###Task:
You have to write a function `pattern` which returns the following Pattern(See Pattern & Examples) upto `n` number of rows. 

* Note:`Returning` the pattern is not the same as `Printing` the pattern.

####Rules/Note:
* If `n < 1` then it should return "" i.e. empty string.
* There are `no whitespaces` in the pattern.

###Pattern: 

    1
    22
    333
    ....
    .....
    nnnnnn
    
###Examples:

+ pattern(5):

      1
      22
      333
      4444
      55555
      
* pattern(11):  

      1
      22
      333
      4444
      55555
      666666
      7777777
      88888888
      999999999
      10101010101010101010
      1111111111111111111111
      
```* Hint: Use \n in string to jump to next line```

<P ALIGN="center"><FONT FACE="Impact"  SIZE="5"><A HREF="http://www.codewars.com/users/curious_db97/authored">>>>LIST OF ALL MY KATAS<<<</A></FONT></P>
"""


def pattern(n):
    return '\n'.join(str(i)*i for i in range(1, n+1))
