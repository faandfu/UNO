from abc import ABC, abstractmethod
from typing import List
from Card import Card
from CardStack import CardStack
from UserInput import UserInput

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
    def __init__(self, user_input:UserInput, card_stack:CardStack) -> None:
        self.cards: List[Card] = []
        self.user_input: UserInput = user_input
        self.card_stack: CardStack = card_stack
    
    def draw_card(self):
        self.cards.append(self.card_stack.draw())

    def play_card(self, current_card: Card) -> Card:
        card = self.user_input.select_card(self.cards)
        self.cards.remove(card)
        return card

    def move(self, current_card:Card) -> Card:
        if(self.user_input.decide_move()):
            return self.play_card(current_card)
        else:
            self.draw_card()
            return current_card


class ComputerPlayer(Player):
    def __init__(self, card_stack:CardStack) -> None:
        self.cards: List[Card] = []
        self.card_stack: CardStack = card_stack
    
    def draw_card(self):
        self.cards.append(self.card_stack.draw())

    def play_card(self, current_card: Card):
        pass 

    def move(self, current_card:Card):
        return current_card