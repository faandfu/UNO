from Card import Card
from typing import List

def get_compatible_cards(cards:List[Card], current_card:Card) -> List[Card]:
    return [card for card in cards if (card.color==current_card.color or card.value == current_card.value)]