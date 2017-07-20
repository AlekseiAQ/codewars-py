"""Currency Matrix Generator
https://www.codewars.com/kata/currency-matrix-generator

On the Forex Market the currency symbols for exchange between two currencies are put together in regards to their strength and weakness. The order of the currency strength is as follows:

"EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"

So for AUD the currency matrix would be as follows
EURAUD, GBPAUD, AUDNZD, AUDUSD, AUDCAD, AUDCHF, AUDJPY

Your goal is to generate this currency matrix for a given currency. You can assume that the passed in currency is a valid one.
"""


def generate_currency_matrix(currency):
    strength_list = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    currency_list = strength_list[:]
    currency_list.remove(currency)
    return [currency + elem
            if strength_list.index(currency) < strength_list.index(elem)
            else elem + currency
            for elem in currency_list]
