from random import randint
from Card import Ability, Card, Color


class CardStack:
    def draw(self):
        ability = randint(0, 100)
        ability = 0 if ability < 80 else ability % 6
        color = Color(randint(1, 4))
        value = randint(0, 9)
        if(ability!=0):
            value = ability+9
        return Card(color, value, Ability(ability))
    
    def shuffle(self):
        pass