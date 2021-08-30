from src.Card import Ability, Card, Color
from typing import List


def get_compatible_cards(cards:List[Card], current_card:Card) -> List[Card]:
    return [card for card in cards if (card.color==current_card.color or card.value == current_card.value or card.ability == Ability.ColorWish or card.ability == Ability.PlusFour)]

def get_best_color(cards:List[Card]):
    red, blue, yellow, green = 0, 0, 0, 0
    for card in cards:
        if(card.color == Color.RED):
            red+=1
        if(card.color == Color.BLUE):
            blue+=1
        if(card.color == Color.GREEN):
            green+=1
        if(card.color == Color.YELLOW):
            yellow+=1
    maxcol = max(red, green, blue, yellow)
    if(red == maxcol):
        return Color.RED
    if(blue == maxcol):
        return Color.BLUE
    if(green == maxcol):
        return Color.GREEN
    if(yellow == maxcol):
        return Color.YELLOW
    