from typing import List
from Card import Card

from Player import ConsolePlayer, Player


class Game:
    def __init__(self) -> None:
        self.players : List[Player]
        self.card_stack : List[Card]
        self.current_card : Card
        
    


