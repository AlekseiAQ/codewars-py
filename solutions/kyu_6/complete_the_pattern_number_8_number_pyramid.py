"""Complete The Pattern #8 - Number Pyramid
https://www.codewars.com/kata/complete-the-pattern-number-8-number-pyramid

###Task:

You have to write a function **pattern** which creates the following Pattern(See Examples) upto n(parameter) number of rows.

####Rules/Note:
* If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
* All the lines in the pattern have same length i.e equal to the number of characters in the last line.
* Range of n is (-∞,100]

###Examples:

pattern(5):

        1    
       121   
      12321  
     1234321 
    123454321


pattern(10):

             1         
            121        
           12321       
          1234321      
         123454321     
        12345654321    
       1234567654321   
      123456787654321  
     12345678987654321 
    1234567890987654321

pattern(15):

                  1              
                 121             
                12321            
               1234321           
              123454321          
             12345654321         
            1234567654321        
           123456787654321       
          12345678987654321      
         1234567890987654321     
        123456789010987654321    
       12345678901210987654321   
      1234567890123210987654321  
     123456789012343210987654321 
    12345678901234543210987654321

pattern(20):

                       1                   
                      121                  
                     12321                 
                    1234321                
                   123454321               
                  12345654321              
                 1234567654321             
                123456787654321            
               12345678987654321           
              1234567890987654321          
             123456789010987654321         
            12345678901210987654321        
           1234567890123210987654321       
          123456789012343210987654321      
         12345678901234543210987654321     
        1234567890123456543210987654321    
       123456789012345676543210987654321   
      12345678901234567876543210987654321  
     1234567890123456789876543210987654321 
    123456789012345678909876543210987654321

###Amazing Fact: 
<img src="http://i1.wp.com/mathandmultimedia.com/wp-content/uploads/2010/11/amazing1.png?resize=600%2C290">

```Hint: Use \n in string to jump to next line```

"""


def make_line(n, i):
    indent = ' ' * (n - i)
    m_line = list(range(1, i+1)) + list(range(i-1, 0, -1))
    m_line = [el % 10 for el in m_line]
    m_line = ''.join(map(str, m_line))
    return indent + m_line + indent

def pattern(n):
    return '\n'.join(make_line(n, i) for i in range(1, n+1))
