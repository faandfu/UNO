from typing import List
from src.Card import Ability, Card
from src.CardStack import CardStack
from src.Display import ConsoleDisplay, Display

from src.Player import ComputerPlayer, Player, UserPlayer
from src.UserInput import ConsoleUserInput, UserInput


class Game:    
    def __init__(self) -> None:
        self.players : List[Player] = []
        self.card_stack : CardStack = CardStack()
        self.current_card : Card = self.card_stack.draw()
        self.display : Display = ConsoleDisplay(self)
        self.user_input : UserInput = ConsoleUserInput()

        self.players.append(UserPlayer(self.user_input, self.card_stack, self.display, "USER"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM1"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM2"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM3"))
        self.players.append(ComputerPlayer(self.card_stack, self.display, "COM4"))

        
        for player in self.players:
            player.draw_card(5)

        
    def run(self):
        playing = True
        player_index = 0
        direction = True
        while(playing):
            
            player = self.players[player_index]  
            if (isinstance(player, UserPlayer)):
                self.display.print_game()
            card = player.move(self.current_card)
            if(card != None):
                self.current_card = card
                if (card.ability == Ability.DirectionChange):
                    direction = not direction
                if (card.ability == Ability.Skip):
                    player_index = (player_index + (1 if direction else -1))
                if (card.ability == Ability.PlusTwo):
                    self.players[(player_index + (1 if direction else -1)) % len(self.players)].draw_card(2)
                if (card.ability == Ability.PlusFour):
                    self.players[(player_index + (1 if direction else -1)) % len(self.players)].draw_card(4)
            if (len(player.cards)==0):
                playing = False
                self.display.message(str(player) + " has won the game!")
                break
            player_index = (player_index + (1 if direction else -1)) % len(self.players) 
                    