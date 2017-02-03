"""Tax Calculator
https://www.codewars.com/kata/tax-calculator

<h1>Write a function to calculate compound tax using the following table:</h1>

<ul>
<li>For $10 and under, the tax rate should be 10%.</li>
<li>For $20 and under, the tax rate on the first $10 is %10, and the tax on the rest is 7%.</li>
<li>For $30 and under, the tax rate on the first $10 is still %10, the rate for the next $10 is still 7%, and everything else is 5%.</li>
<li>Tack on an additional 3% for the portion of the total above $30.</li>
<li>Return 0 for invalid input(anything that's not a positive real number).
</li>
</ul>
<h2>Examples:</h2>
<ul>
<li>An input of 10, should return 1 (1 is 10% of 10)</li>
<li>An input of 21, should return 1.75 (10% of 10 + 7% of 10 + 5% of 1)</li>
</ul>
<p>* Note that the returned value should be rounded to the nearest penny.</p>

"""


def tax_calculator(total):
    if not isinstance(total, (int, float)) or total <= 0:
        return 0
    elif total <= 10:
        return round(total * 0.1, 2)
    elif total <= 20:
        return round(1 + (total - 10) * 0.07, 2)
    elif total <= 30:
        return round(1.7 + (total - 20) * 0.05, 2)
    else:
        return round(2.2 + (total - 30) * 0.03, 2)
