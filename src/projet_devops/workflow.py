ALLOWED_TRANSITIONS = {
    "CREATED": {"PAID", "CANCELLED"},
    "PAID": {"PREPARING", "CANCELLED"},
    "PREPARING": {"SHIPPED"},
    "SHIPPED": {"DELIVERED"},
    "DELIVERED": set(),
    "CANCELLED": set(),
}


def validate_status_transition(current_status: str, new_status: str) -> None:
    """
    Valide une transition de statut.
    Lève une ValueError si la transition est invalide.
    """
    if current_status not in ALLOWED_TRANSITIONS:
        raise ValueError(f"Unknown status: {current_status}")

    if new_status not in ALLOWED_TRANSITIONS[current_status]:
        raise ValueError(
            f"Invalid transition from {current_status} to {new_status}"
        )
