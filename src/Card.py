from enum import Enum
from dataclasses import dataclass

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

@dataclass
class Card:
    color: Color
    value: int

    def __str__(self) -> str:
        return self.color.name + " " + str(self.value)