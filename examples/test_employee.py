import pytest

from employee import BankAccount, Employee


@pytest.fixture
def bank_account():
    return BankAccount("MyBank", 10)


@pytest.fixture
def employee(bank_account):
    return Employee("Anna Smith", bank_account, 1000)


@pytest.mark.parametrize("percent,expected_salary", [
    (5, 1050), (10, 1100), (20, 1200)
])
def test_valid_raise_percent(employee, percent, expected_salary):
    employee.raise_salary(percent)
    assert employee.salary == expected_salary


def test_invalid_raise_percent(employee):
    with pytest.raises(ValueError):
        employee.raise_salary(50)
    assert employee.salary == 1000
