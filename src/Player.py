from abc import ABC, abstractmethod
from random import randint
from typing import List
from Card import Card
from CardStack import CardStack
from Display import Display
from UserInput import UserInput
from Helper import get_compatible_cards

class Player(ABC):
    @abstractmethod
    def play_card(self, current_card:Card) -> Card:
        pass
    
    @abstractmethod
    def draw_card(self):
        pass

    @abstractmethod
    def move(self, current_card:Card) -> Card:
        pass

class UserPlayer(Player):
    def __init__(self, user_input:UserInput, card_stack:CardStack, display:Display, name:str) -> None:
        self.cards: List[Card] = []
        self.user_input: UserInput = user_input
        self.card_stack: CardStack = card_stack
        self.display = display
        self.name = name
    
    def draw_card(self):
        self.cards.append(self.card_stack.draw())

    def play_card(self, current_card: Card) -> Card:
        compatible_cards = get_compatible_cards(self.cards, current_card)
        if(len(compatible_cards) == 0):
            self.display.message("No valid options, you have to draw a card.")
            self.draw_card()
            card = current_card
            return card
        card = self.user_input.select_card(self.cards)
        if(not (card in compatible_cards)):
            self.user_input.message("Card not valid. Try again.")
            card = self.move(current_card)
        else:
            self.cards.remove(card)
        return card

    def move(self, current_card:Card) -> Card:
        if(self.user_input.decide_move()):
            return self.play_card(current_card)
        else:
            self.draw_card()
            return current_card
    
    def __str__(self) -> str:
        return self.name


class ComputerPlayer(Player):
    def __init__(self, card_stack:CardStack, display:Display, name:str) -> None:
        self.cards: List[Card] = []
        self.card_stack: CardStack = card_stack
        self.display = display
        self.name = name
    
    def draw_card(self):
        self.cards.append(self.card_stack.draw())

    def play_card(self, current_card: Card):
        compatible_cards = get_compatible_cards(self.cards, current_card)
        if(len(compatible_cards) == 0):
            self.display.message(self.name + " had to draw a card.")
            self.draw_card()
            card = current_card 
        else:
            card = compatible_cards[randint(0, len(compatible_cards)-1)]
            self.cards.remove(card)
            self.display.message(self.name + " played " + str(card))
        return card

    def move(self, current_card:Card):
        return self.play_card(current_card)
    
    def __str__(self) -> str:
        return self.name