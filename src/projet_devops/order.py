from typing import List, Dict


def calculate_order_total(items: List[Dict]) -> float:
    """
    Calcule le total d'une commande à partir d'une liste d'items.
    Chaque item doit contenir :
      - unit_price (float >= 0)
      - quantity (int >= 0)
    """
    total = 0.0

    for item in items:
        unit_price = item.get("unit_price")
        quantity = item.get("quantity")

        if unit_price is None or quantity is None:
            raise ValueError("Item must contain unit_price and quantity")

        if unit_price < 0 or quantity < 0:
            raise ValueError("unit_price and quantity must be non-negative")

        total += unit_price * quantity

    return round(total, 2)
