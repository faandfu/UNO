from src.Helper import *
from src.Player import Player, UserPlayer
from src.CardStack import CardStack
from src.Card import Card
from src.UserInput import ConsoleUserInput
from src.Display import ConsoleDisplay
from src.Game import Game
import pytest


@pytest.fixture
def player1():
    game = Game()
    card_stack : CardStack = CardStack()
    display = ConsoleDisplay(game)
    user_input = ConsoleUserInput()
    player = UserPlayer(user_input, card_stack, display, "TestUser")
    return player

def test_user_player_draw_card(player1: UserPlayer):    
    player1.draw_card()
    assert 1 == len(player1.cards)

def test_user_player_name(player1: UserPlayer):    
    assert str(player1) == "TestUser"

def test_user_player_move(player1: UserPlayer):  
    card = Card(1,1)  
    assert player1.move(card) == None