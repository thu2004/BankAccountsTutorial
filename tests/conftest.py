import pytest

from bank_accounts_tutorial.bank_account import BankAccount
from bank_accounts_tutorial.savings_account import SavingsAccount
from bank_accounts_tutorial.fee_savings_account import FeeSavingsAccount

PIN = "1234"
WRONG_PIN = "0000"


@pytest.fixture()
def bank_account():
    yield BankAccount(PIN)


@pytest.fixture()
def saving_bank_account():
    yield SavingsAccount(PIN)


@pytest.fixture()
def zero_fee_saving_bank_account():
    yield FeeSavingsAccount(PIN)


@pytest.fixture()
def ten_fee_saving_bank_account():
    yield FeeSavingsAccount(PIN, fee=10)
