import pytest
import adventure
import io
import sys
from unittest.mock import patch
from io import StringIO

# --- Week 4 Specific Tests ---


# Test display_inventory function - empty inventory
def test_display_inventory_empty(capsys):
    inventory = []
    adventure.display_inventory(inventory)
    captured = capsys.readouterr()
    assert "Your inventory is empty." in captured.out