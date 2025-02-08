import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys


# Test enter_dungeon - trap challenge failure
def test_enter_dungeon_trap_failure(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "disarm") # Choose to disarm trap
    monkeypatch.setattr('random.choice', lambda _: False) # Force trap failure
    initial_health = 60
    dungeon_rooms_test_trap = [
        ("A trapped hallway", None, "trap", ("Trap disarmed!", "You triggered the trap!", -15)),
    ]
    updated_health, _ = adventure.enter_dungeon(initial_health, [], dungeon_rooms_test_trap)
    assert updated_health == 45 # Health should decrease by 15
    captured = capsys.readouterr()
    assert "You see a potential trap!" in captured.out
    assert "You triggered the trap!" in captured.out