import pytest
import adventure
import io
import sys
from unittest.mock import patch
from io import StringIO

# --- Week 4 Specific Tests ---

# Test enter_dungeon - item acquisition
def test_enter_dungeon_item_acquisition(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "move on") # No interaction needed for item room
    initial_inventory = []
    dungeon_rooms_test_item = [
        ("A treasure room", "gold coins", "none", None),
    ]
    _, final_inventory = adventure.enter_dungeon(100, initial_inventory, dungeon_rooms_test_item)
    assert "gold coins" in final_inventory
    captured = capsys.readouterr()
    assert "You found a gold coins in the room." in captured.out
    assert "You acquired a gold coins!" in captured.out