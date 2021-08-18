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

        #self.players.append(UserPlayer(self.user_input, self.card_stack, self.display, "USER"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM1"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM2"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM3"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM4"))

        for i in range(5000):
            for player in self.players:
                player.draw_card()

        
    def run(self):
        playing = True
        while(playing):
            #self.display.print_game()
            for player in self.players:                
                self.current_card = player.move(self.current_card)
                if(len(player.cards)==1):
                    self.display.message("--UNO--")
                elif (len(player.cards)==0):
                    playing = False
                    self.display.message(str(player) + " has won the game!")
                    break
                    
            

    

    


