from unittest import TestCase


def test_name():
    p = Player("TestPlayer")

    assert p.name == "TestPlayer"
    assert p.score == 0

    p.add_score(10)
    assert p.get_score() == 10

    p.add_score(5)
    assert p.get_score() == 15


import pytest
from Board import Board
from Player import Player


def test_board():
    with pytest.raises(ValueError, match='n must be an int'):
        b = Board("two", '2')
    with pytest.raises(ValueError, match='n must not be less than 2'):
        b = Board(1, '5')
    with pytest.raises(ValueError, match='t must be digit'):
        b = Board(2, 'three')
    with pytest.raises(ValueError, match='t must be digit greater 0'):
        b = Board(2, '-3')




