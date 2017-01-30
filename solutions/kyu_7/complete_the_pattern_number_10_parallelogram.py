"""Complete The Pattern #10 - Parallelogram
https://www.codewars.com/kata/complete-the-pattern-number-10-parallelogram

###Task:

You have to write a function **pattern** which returns the following Pattern(See Examples) upto n rows, where n is parameter.

####Rules/Note:
* If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
* The length of each line = (2n-1).
* Range of n is (-∞,100]

###Examples:

pattern(5):

        12345
       12345 
      12345  
     12345   
    12345    

pattern(10):

             1234567890
            1234567890 
           1234567890  
          1234567890   
         1234567890    
        1234567890     
       1234567890      
      1234567890       
     1234567890        
    1234567890         

pattern(15):

                  123456789012345
                 123456789012345 
                123456789012345  
               123456789012345   
              123456789012345    
             123456789012345     
            123456789012345      
           123456789012345       
          123456789012345        
         123456789012345         
        123456789012345          
       123456789012345           
      123456789012345            
     123456789012345             
    123456789012345              

pattern(20):

                       12345678901234567890
                      12345678901234567890 
                     12345678901234567890  
                    12345678901234567890   
                   12345678901234567890    
                  12345678901234567890     
                 12345678901234567890      
                12345678901234567890       
               12345678901234567890        
              12345678901234567890         
             12345678901234567890          
            12345678901234567890           
           12345678901234567890            
          12345678901234567890             
         12345678901234567890              
        12345678901234567890               
       12345678901234567890                
      12345678901234567890                 
     12345678901234567890                  
    12345678901234567890                   

"""


def make_line(n, s, i):
    return ' ' * (n - i) + s + ' ' * (i - 1)


def pattern(n):
    s = ''.join(str(i % 10) for i in range(1, n+1))
    return '\n'.join(make_line(n, s, i) for i in range(1, n+1))
