Bank Account Kata
-----------------
See the [original kata](https://www.codurance.com/katas/bank).

# Requirements
Create a simple bank application with the following features:

* Deposit into Account
* Withdraw from an Account
* Print a bank statement to the console

# Acceptance Criteria
Statement should have the following format:
```text
Date       | Amount  | Balance
10/04/2014 | 500.00  | 1400.00
02/04/2014 | -100.00 | 900.00
01/04/2014 | 1000.00 | 1000.00
```

# Rules
* You cannot change the public interface of any class.
* Use Strings and Integers for dates and amounts (no need for `datetime` or `float` types).

# Starting Point
Here is a starting point for your Bank application in Python:

```python
class Account:
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def print_statement(self):
        pass

```
		
# Example Usage
```python
account = Account()
account.deposit(1000)
account.withdraw(100)
account.deposit(500)
account.print_statement()
```

# Expected output:

```text
Date       | Amount  | Balance
10/04/2014 | 500.00  | 1400.00
02/04/2014 | -100.00 | 900.00
01/04/2014 | 1000.00 | 1000.00
```
		
# Tips
* Focus on getting the basic functionality working first.
* Write tests to cover the functionality.
* Refactor your code to improve readability and maintainability.
* Ensure your code follows good design principles.
