import pytest
from bank_accounts_tutorial.bank_account import BankAccount

PIN = "1234"
WRONG_PIN = "0000"


def test_valid_pin(bank_account):

    # Arrange
    #

    # Act
    bank_account.deposit(PIN, 100)
    bank_account.withdraw(PIN, 50)
    bank_account.get_balance(PIN)
    bank_account.change_pin(PIN, 1111)


def test_invalid_pin_deposit(bank_account):
    # Arrange

    with pytest.raises(RuntimeError) as excinfo:
        # Act
        bank_account.deposit(WRONG_PIN, 100)
        excinfo == "The pin not match"


def test_invalid_pin_withdraw(bank_account):
    # Arrange

    with pytest.raises(RuntimeError) as excinfo:
        # Act
        bank_account.withdraw("1111", 100)
        excinfo == "The pin not match"


def test_invalid_pin_get_balance(bank_account):
    # Arrange

    with pytest.raises(RuntimeError) as excinfo:
        # Act
        bank_account.get_balance("1111")
        excinfo == "The pin not match"


def test_invalid_pin_change_pin(bank_account):
    # Arrange

    with pytest.raises(RuntimeError) as excinfo:
        # Act
        bank_account.change_pin("1111", "100")
        excinfo == "The pin not match"


## deposit


def test_deposit(bank_account):
    # Arrange

    # Act
    bank_account.deposit(PIN, 100)

    # Assert

    assert bank_account._balance == 100


def test_deposit_exception(bank_account):
    with pytest.raises(RuntimeError) as excinfo:

        # Arrange

        # Act
        bank_account.deposit(PIN, -100)

        # Assert
        assert "Can not deposit less than 0" == str(excinfo.value)


## withdraw


def test_withdraw(bank_account):
    # Arrange
    bank_account.deposit(PIN, 500)

    # Act
    bank_account.withdraw(PIN, 400)

    # Assert

    assert bank_account._balance == 100


def test_withdraw_exception(bank_account):
    with pytest.raises(RuntimeError) as excinfo:

        # Arrange
        my_account = BankAccount(PIN, 100)

        # Act
        bank_account.withdraw(PIN, 200)

        # Assert
        assert "operation can not be done as amount  > balance" == str(excinfo.value)


## get balance


def test_get_balance(bank_account):
    # Arrange

    # Act
    bank_account.deposit(PIN, 100)

    # Assert

    assert bank_account.get_balance(PIN) == 100


## change pin


def test_change_pin(bank_account):
    # Arrange
    bank_account.deposit(PIN, 100)

    NEW_PIN = "1230"

    # Act
    bank_account.change_pin(PIN, NEW_PIN)

    # Assert

    assert bank_account.get_balance(NEW_PIN) == 100
