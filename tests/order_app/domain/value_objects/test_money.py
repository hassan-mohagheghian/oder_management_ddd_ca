from decimal import Decimal

import pytest

from order_app.domain.value_objects.money import Money


def test_money_creation():
    amount = Money(Decimal("100"))
    assert amount.amount == Decimal("100")


def test_money_equality():
    money1 = Money(Decimal("50"))
    money2 = Money(Decimal("50"))
    money3 = Money(Decimal("75"))
    assert money1 == money2
    assert money1 != money3


def test_money_negative_amount():
    with pytest.raises(ValueError, match="Money amount cannot be negative"):
        Money(Decimal("-20"))


def test_money_addition():
    money1 = Money(Decimal("50"))
    money2 = Money(Decimal("70"))
    total = money1 + money2
    assert total.amount == Decimal("120")


def test_money_multiplication_int():
    money1 = Money(Decimal("50"))
    total = money1 * 2
    assert total.amount == Decimal("100")


def test_money_multiplication_decimal():
    money1 = Money(Decimal("50"))
    total = money1 * Decimal(0.5)
    assert total.amount == Decimal("25")


def test_money_multiplication_invalid_type():
    money1 = Money(Decimal("50"))
    value = 0.5
    with pytest.raises(TypeError, match=f"Cannot multiply Money by {type(value)}"):
        money1 * value
    value = "0.5"
    with pytest.raises(TypeError, match=f"Cannot multiply Money by {type(value)}"):
        money1 * value


def test_money_precision():
    money = Money(Decimal("99.99"))
    assert money.amount == Decimal("99.99")

    money2 = Money(Decimal("0.019"))
    assert money2.amount == Decimal("0.02")


def test_money_str_representation():
    money = Money(Decimal("150"))
    assert str(money) == "150.00 USD"
