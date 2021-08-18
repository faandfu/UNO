from random import randint
from Card import Card, Color


class CardStack:
    def draw(self):
        return Card(color=Color(randint(1, 4)), value=randint(0, 9))
    
    def shuffle(self):
        pass