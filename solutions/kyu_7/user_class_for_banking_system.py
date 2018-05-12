"""User class for Banking System
https://www.codewars.com/kata/user-class-for-banking-system

A company is opening a bank, but the coder who is designing the user class made some errors. They need <strong> you </strong> to help them.

You <strong>must</strong> include the following:

- A withdraw method
  - Subtracts money from balance
  - One parameter, money to withdraw
  - Raise ValueError if there isn't enough money to withdraw
  - Return a string with name and balence(see examples)

* A check method
  - Adds money to baleance
  - Two parameters, other user and money
  - Other user will always be valid
  - Raise a ValueError if other user doesn't have enough money
  - Raise a ValueError if checking_account isn't true for other user
  - Return a string with name and balance plus other name and other balance(see examples)

- An add_cash method
  - Adds money to balance
  - One parameter, money to add
  - Return a string with name and balance(see examples)

Additional Notes:
  * Checking_account should be stored as a boolean
  - No input numbers will be negitive
  * Output must end with period
  - Float numbers will not be used so, balance should be integer
  * No currency will be used

Examples:
``` Python
Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

Jeff.withdraw(2) # Returns 'Jeff has 68.'

Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

Joe.check(Jeff, 100) # Raises a ValueError

Jeff.add_cash(20.00) # Returns 'Jeff has 118.'
```

<h1 align = 'Center'><font size = '7'><strong> Good Luck </strong></font></h1>
"""


class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("{} doesn't have enough money.".format(self.name))
        self.balance -= amount
        return self.get_balance_message()

    def check(self, other_user, amount):
        if not other_user.checking_account:
            raise ValueError(
                "{}'s checking account is disabled.".format(self.name))
        message_one, message_two = \
            other_user.withdraw(amount), self.add_cash(amount)[:-1]
        return '{} and {}'.format(message_two, message_one)

    def add_cash(self, amount):
        self.balance += amount
        return self.get_balance_message()

    def get_balance_message(self):
        return '{} has {}.'.format(self.name, self.balance)
