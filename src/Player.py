from abc import ABC, abstractmethod
from typing import List
from Card import Card

class Player(ABC):
    @abstractmethod
    def play_card(self):
        pass
    
    @abstractmethod
    def draw_card(self):
        pass

    @abstractmethod
    def move(self):
        pass

class ConsolePlayer(Player):
    def __init__(self, card_stack) -> None:
        self.cards: List[Card]
        self.card_stack: List[Card] = card_stack
    
    def draw_card(self):
        self.cards.append(self.card_stack.pop(0))

    def play_card(self, last_card: Card):
        pass 

    def move(self):
        pass


class ComputerPlayer(Player):
    def __init__(self, card_stack) -> None:
        self.cards: List[Card]
        self.card_stack: List[Card] = card_stack
    
    def draw_card(self):
        self.cards.append(self.card_stack.pop(0))

    def play_card(self, last_card: Card):
        pass 

    def move(self):
        pass