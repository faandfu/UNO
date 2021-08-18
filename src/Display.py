from abc import ABC, abstractmethod



class Display(ABC):
    @abstractmethod
    def print_game(self):
        pass


class ConsoleDisplay(Display):
    def __init__(self, game) -> None:
        self.game = game
    
    def print_game(self):
        print("\nUNO \n \t\t\t" + str(self.game.current_card) + "\n\n\n" + str([str(card) for card in self.game.players[0].cards]))