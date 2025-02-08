import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys

# Test enter_dungeon - no challenge room
def test_enter_dungeon_no_challenge(capsys):
    dungeon_rooms_test_none = [
        ("A peaceful clearing", None, "none", None),
    ]
    adventure.enter_dungeon(100, [], dungeon_rooms_test_none)
    captured = capsys.readouterr()
    assert "There doesn't seem to be a challenge in this room." in captured.out
    assert "A peaceful clearing" in captured.out # Check room description is printed