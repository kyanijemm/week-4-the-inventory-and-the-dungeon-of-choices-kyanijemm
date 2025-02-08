import pytest
import adventure
import io
import sys
from unittest.mock import patch
from io import StringIO

# --- Week 4 Specific Tests ---

# Test acquire_item function
def test_acquire_item_adds_item_and_returns_inventory():
    inventory = []
    updated_inventory = adventure.acquire_item(inventory, "torch")
    assert "torch" in updated_inventory
    assert isinstance(updated_inventory, list) # Verify it returns a list