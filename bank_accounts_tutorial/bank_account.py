class BankAccount:
    """Bank Account protected by a pin number."""

    def __init__(self, pin, balance=0):
        """Initial account balance is 0 and pin is 'pin'."""
        self._pin = pin
        self._balance = balance

    def deposit(self, pin, amount):
        self._check_pin(pin)
        if amount < 0:
            raise RuntimeError("Can not deposit less than 0")
        self._balance = self._balance + amount
        return self._balance

    def withdraw(self, pin, amount):
        self._check_pin(pin)
        if self._balance >= amount:
            self._balance = self._balance - amount
            return amount
        else:
            raise RuntimeError("operation can not be done as amount  > balance ")

    def get_balance(self, pin):
        """Return account balance."""
        self._check_pin(pin)
        return self._balance

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        self._check_pin(oldpin)
        self._pin = newpin

    def _check_pin(self, pin_to_check):
        if pin_to_check != self._pin:
            raise RuntimeError("The pin not match")
