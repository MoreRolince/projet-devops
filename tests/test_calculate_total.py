import pytest
from order_management.services import calculate_order_total


def test_calculate_total_nominal():
    items = [
        {"price": 10.0, "quantity": 2},
        {"price": 5.5, "quantity": 1},
    ]
    assert calculate_order_total(items) == 25.5


def test_calculate_total_empty():
    with pytest.raises(ValueError):
        calculate_order_total([])


def test_calculate_total_invalid_price():
    items = [{"price": -1, "quantity": 1}]
    with pytest.raises(ValueError):
        calculate_order_total(items)


def test_calculate_total_missing_field():
    items = [{"price": 10}]
    with pytest.raises(ValueError):
        calculate_order_total(items)
