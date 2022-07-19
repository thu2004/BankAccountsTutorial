import pytest
from bank_accounts_tutorial.fee_savings_account import FeeSavingsAccount

PIN = "1234"


def test_withdraw_with_no_fee(zero_fee_saving_bank_account):
    # Arrange
    zero_fee_saving_bank_account.deposit(PIN, 500)

    # Act
    zero_fee_saving_bank_account.withdraw(PIN, 400)

    # Assert
    assert zero_fee_saving_bank_account._balance == 100


def test_withdraw_with_fee(ten_fee_saving_bank_account):
    # Arrange
    ten_fee_saving_bank_account.deposit(PIN, 500)

    # Act
    ten_fee_saving_bank_account.withdraw(PIN, 400)

    # Assert
    assert ten_fee_saving_bank_account._balance == 90


def test_withdraw_exception(zero_fee_saving_bank_account):
    with pytest.raises(RuntimeError) as excinfo:
        # Act
        zero_fee_saving_bank_account.withdraw(PIN, 200)

        # Assert
        assert "operation can not be done as amount  > balance" == str(excinfo.value)

    with pytest.raises(RuntimeError) as excinfo:

        # Arrange

        # Act
        zero_fee_saving_bank_account.increase(PIN, -50)

        # Assert

        assert "rate should be > 0" == str(excinfo.value)
