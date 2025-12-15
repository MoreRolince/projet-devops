import pytest
from projet_devops.order import calculate_order_total


def test_calculate_order_total_nominal():
    items = [
        {"unit_price": 10.0, "quantity": 2},
        {"unit_price": 5.5, "quantity": 1},
    ]
    assert calculate_order_total(items) == 25.5


def test_calculate_order_total_empty():
    assert calculate_order_total([]) == 0.0


def test_calculate_order_total_negative_price():
    items = [{"unit_price": -1.0, "quantity": 1}]
    with pytest.raises(ValueError):
        calculate_order_total(items)


def test_calculate_order_total_missing_field():
    items = [{"unit_price": 10.0}]
    with pytest.raises(ValueError):
        calculate_order_total(items)
