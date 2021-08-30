from abc import ABC, abstractmethod
from random import randint
from typing import List
from src.Card import Ability, Card
from src.CardStack import CardStack
from src.Display import Display
from src.UserInput import UserInput
from src.Helper import get_best_color, get_compatible_cards

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
    
    def draw_card(self, num=1):
        for i in range(num):
            self.cards.append(self.card_stack.draw())

    def play_card(self, current_card: Card, compatible_cards:List[Card]) -> Card:
        card = self.user_input.select_card(self.cards)
        if(not (card in compatible_cards)):
            self.display.message("Card not valid. Try again.")
            card = self.move(current_card)
        else:
            self.cards.remove(card)
            if(card.ability == Ability.ColorWish or card.ability == Ability.PlusFour):
                card.color = get_best_color(self.cards)
        
            if(len(self.cards)==1):
                self.display.message(str(self) + "---UNO---")
        return card

    def move(self, current_card:Card) -> Card:
        compatible_cards = get_compatible_cards(self.cards, current_card)
        if(len(compatible_cards) == 0):
            self.display.message("No valid options, you have to draw a card.")
            self.draw_card()
            return None
        if(self.user_input.decide_move()):
            return self.play_card(current_card, compatible_cards)
        else:
            self.draw_card()
            return None
    
    def __str__(self) -> str:
        return self.name


class ComputerPlayer(Player):
    def __init__(self, card_stack:CardStack, display:Display, name:str) -> None:
        self.cards: List[Card] = []
        self.card_stack: CardStack = card_stack
        self.display = display
        self.name = name
    
    def draw_card(self, num=1):
        for i in range(num):
            self.cards.append(self.card_stack.draw())

    def play_card(self, compatible_cards:List[Card]):
        card = compatible_cards[randint(0, len(compatible_cards)-1)]
        self.cards.remove(card)
        if(card.ability == Ability.ColorWish or card.ability == Ability.PlusFour):
            card.color = get_best_color(self.cards)
        self.display.message(self.name + " played " + str(card))
        if(len(self.cards)==1):
            self.display.message(str(self) + " ---UNO---")
        return card

    def move(self, current_card:Card):
        compatible_cards = get_compatible_cards(self.cards, current_card)
        if(len(compatible_cards) == 0):
            self.display.message(self.name + " had to draw a card.")
            self.draw_card()
            return None
        else:
            return self.play_card(compatible_cards)
        
    
    def __str__(self) -> str:
        return self.name
