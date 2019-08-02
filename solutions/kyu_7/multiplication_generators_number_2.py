"""Multiplication - Generators #2
https://www.codewars.com/kata/multiplication-generators-number-2

<h1>Multiplication - Generators #2</h1>
Generators can be used to wonderful things. You can use them for numerous things, but here is one specific example. You are studying for a test so you must practice your multiplication, but you don't have a multiplication table showing the different examples. You have decided to create a generator that prints out a limitless list of time tables.

<h2>Task</h2>
<p>
Your generator must take one parameter `a` then everytime the generator is called you must return a string in the format of: `'a x b = c'` where c is the answer. Also, the value of `b`, which starts at 1, must increment by 1 each time!
</p>

<strong>More Info: </strong>[Generators (JS)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators), <a href="https://wiki.python.org/moin/Generators">Generators (Python)</a>, [Generators (PHP)](http://php.net/manual/en/language.generators.php), [Generators (Java)](https://thecannycoder.wordpress.com/2014/07/04/generators/)
"""


def generator(a):
    store = 1
    while True:
        yield f"{a} x {store} = {a * store}"
        store += 1
