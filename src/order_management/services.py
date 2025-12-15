from typing import List, Dict
from .models import OrderStatus


def calculate_order_total(items: List[Dict]) -> float:
    """
    Calcule le total d'une commande.
    Chaque item doit contenir 'price' (>0) et 'quantity' (>0).
    """
    if not items:
        raise ValueError("Order must contain at least one item")

    total = 0.0
    for item in items:
        price = item.get("price")
        quantity = item.get("quantity")

        if price is None or quantity is None:
            raise ValueError("Item must have price and quantity")
        if price <= 0 or quantity <= 0:
            raise ValueError("Price and quantity must be positive")

        total += price * quantity

    return round(total, 2)


def validate_status_transition(
    current_status: OrderStatus,
    new_status: OrderStatus,
) -> bool:
    """
    Valide une transition de statut de commande.
    """
    allowed_transitions = {
        OrderStatus.CREATED: {OrderStatus.PAID, OrderStatus.CANCELLED},
        OrderStatus.PAID: {OrderStatus.SHIPPED},
        OrderStatus.SHIPPED: set(),
        OrderStatus.CANCELLED: set(),
    }

    return new_status in allowed_transitions[current_status]
