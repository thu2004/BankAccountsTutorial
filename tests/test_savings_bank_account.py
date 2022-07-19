import pytest
from bank_accounts_tutorial.savings_account import SavingsAccount

PIN = "1234"


def test_valid_pin(saving_bank_account):
    saving_bank_account.increase(PIN, 30)


def test_invalid_pin(saving_bank_account):
    with pytest.raises(RuntimeError) as excinfo:
        # Act
        saving_bank_account.increase("1111", 100)
        excinfo == "The pin not match"


def test_increase(saving_bank_account):
    # Arrange
    saving_bank_account.deposit(PIN, 100)

    # Act
    saving_bank_account.increase(PIN, 50)

    # Assert
    assert saving_bank_account._balance == 150


def test_increase_exception(saving_bank_account):
    with pytest.raises(RuntimeError) as excinfo:
        # Act
        saving_bank_account.increase(PIN, -50)

        # Assert
        assert "rate should be > 0" == str(excinfo.value)
