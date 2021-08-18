from enum import Enum
from dataclasses import dataclass

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

class Ability(Enum):
    NoAbility = 0    
    DirectionChange = 1
    PlusTwo = 2
    PlusFour = 3
    ColorWish = 4
    Skip = 5


@dataclass
class Card:
    color: Color
    value: int
    ability: Ability = Ability.NoAbility

    def __str__(self) -> str:
        if (self.ability == Ability.NoAbility):
            return self.color.name + " " + str(self.value)
        else:
            return self.color.name + " " + self.ability.name

