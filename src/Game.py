from typing import List
from Card import Card
from CardStack import CardStack
from Display import ConsoleDisplay, Display

from Player import ComputerPlayer, Player, UserPlayer
from UserInput import ConsoleUserInput, UserInput


class Game:    
    def __init__(self) -> None:
        self.players : List[Player] = []
        self.card_stack : CardStack = CardStack()
        self.current_card : Card = self.card_stack.draw()
        self.display : Display = ConsoleDisplay(self)
        self.user_input : UserInput = ConsoleUserInput()

        self.players.append(UserPlayer(self.user_input, self.card_stack))
        self.players.append(ComputerPlayer(self.card_stack))
        self.players.append(ComputerPlayer(self.card_stack))

        for i in range(5):
            for player in self.players:
                player.draw_card()

        
    def run(self):
        self.display.print_game()
        while(True):
            for player in self.players:                
                self.current_card = player.move(self.current_card)
            self.display.print_game()

    

    


