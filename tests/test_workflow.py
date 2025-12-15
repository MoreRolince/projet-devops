import pytest
from projet_devops.workflow import validate_status_transition


def test_valid_transition():
    validate_status_transition("CREATED", "PAID")


def test_invalid_transition():
    with pytest.raises(ValueError):
        validate_status_transition("DELIVERED", "PAID")


def test_unknown_status():
    with pytest.raises(ValueError):
        validate_status_transition("UNKNOWN", "CREATED")
