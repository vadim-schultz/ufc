class Account:
    def __init__(self):
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def print_statement(self):
        pass


def test_account():
    account = Account()
    account.deposit(1000)
    account.deposit(2000)
    account.withdraw(500)
    output = account.print_statement()

    expected_output = \
"""
Date       | Amount  | Balance
10/04/2014 | -500    | 2500
02/04/2014 | 2000    | 3000
01/04/2014 | 1000    | 1000
"""
    assert output == expected_output