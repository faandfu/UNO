from abc import ABC, abstractmethod
from src.Card import Card
from typing import List


class UserInput(ABC):
    @abstractmethod
    def select_card(self, cards: List[Card]) -> Card:
        pass

    def decide_move(self) -> bool:
        pass


class ConsoleUserInput(UserInput):
    def __init__(self) -> None:
        pass
        # self.player : UserPlayer = player

    def select_card(self, cards):
        print("Select Card to play [0," + str(len(cards) - 1) + "]")
        return cards[int(input())]

    def decide_move(self) -> bool:
        print("Play Card or draw Card(p/d)?")
        if input() == "p":
            return True
        else:
            return False
