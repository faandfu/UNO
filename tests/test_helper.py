from src.Helper import *
from src.Card import Card, Color, Ability
import pytest


@pytest.fixture
def cards():
    cards: List[Card] = []
    cards.append(Card(Color.RED, 1))
    cards.append(Card(Color.RED, 1))
    cards.append(Card(Color.RED, 2))
    cards.append(Card(Color.RED, 4))
    cards.append(Card(Color.GREEN, 2))
    cards.append(Card(Color.YELLOW, 4))

    return cards


def test_get_compatible_cards(cards):
    current_card = Card(Color.RED, 4)
    compatible = get_compatible_cards(cards, current_card)
    assert len(compatible) == 5
    assert cards[0] in compatible


def test_get_best_color(cards):
    assert Color.RED == get_best_color(cards)
