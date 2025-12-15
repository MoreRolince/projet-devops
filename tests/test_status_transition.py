from order_management.models import OrderStatus
from order_management.services import validate_status_transition


def test_valid_transition():
    assert validate_status_transition(
        OrderStatus.CREATED, OrderStatus.PAID
    ) is True


def test_invalid_transition():
    assert validate_status_transition(
        OrderStatus.CREATED, OrderStatus.SHIPPED
    ) is False


def test_terminal_status():
    assert validate_status_transition(
        OrderStatus.CANCELLED, OrderStatus.CREATED
    ) is False
