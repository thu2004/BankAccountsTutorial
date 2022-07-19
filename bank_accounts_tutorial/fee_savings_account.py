from bank_accounts_tutorial.savings_account import SavingsAccount


class FeeSavingsAccount(SavingsAccount):
    """Free Savings Account protected by a pin number."""

    def __init__(self, pin, balance=0, fee=0):
        """Initial Free Savings account balance is 0 and pin is 'pin', fee charge of withdraw ."""
        super().__init__(pin, balance)
        self._fee = fee

    def withdraw(self, pin, amount):

        """Decrement account balance by amount and return amount withdrawn."""
        self._check_pin(pin)
        if self._balance >= (amount + self._fee):
            self._balance = self._balance - (amount + self._fee)
            return amount
        else:
            raise RuntimeError("operation can not be done as amount + fee  > balance ")
