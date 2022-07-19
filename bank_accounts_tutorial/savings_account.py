from bank_accounts_tutorial.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """Savings Account protected by a pin number."""

    def increase(self, pin, rate):
        """Increment account balance by amount and return new balance."""
        self._check_pin(pin)
        if rate > 0:
            self._balance = self._balance + int(self._balance * rate / 100)
        else:
            raise RuntimeError("rate should be > 0 ")
