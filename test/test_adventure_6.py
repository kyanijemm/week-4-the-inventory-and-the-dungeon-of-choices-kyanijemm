import pytest
import adventure
import io
import sys
from unittest.mock import patch
from io import StringIO

# --- Week 4 Specific Tests ---

# Test display_inventory function - with items
def test_display_inventory_with_items(capsys):
    inventory = ["rope", "grappling hook", "potion"]
    adventure.display_inventory(inventory)
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n') # Split output into lines
    assert "Your inventory:" in output_lines[0]
    assert "1. rope" in output_lines[1]
    assert "2. grappling hook" in output_lines[2]
    assert "3. potion" in output_lines[3]