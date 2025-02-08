import pytest
import adventure
import random
from unittest.mock import patch
from io import StringIO
import sys
# Test enter_dungeon - puzzle challenge success
def test_enter_dungeon_puzzle_success(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "solve") # Choose to solve puzzle
    monkeypatch.setattr('random.choice', lambda _: True) # Force puzzle success
    initial_health = 50
    dungeon_rooms_test_puzzle = [
        ("A puzzle chamber", None, "puzzle", ("Puzzle solved!", "Puzzle failed!", -10)),
    ]
    updated_health, _ = adventure.enter_dungeon(initial_health, [], dungeon_rooms_test_puzzle)
    assert updated_health == 40 # Health should decrease by 10 as per challenge outcome in example
    captured = capsys.readouterr()
    assert "You encounter a puzzle!" in captured.out
    assert "Puzzle solved!" in captured.out