from side import Side
from typing import Dict

class Room(Side):

    total_rooms: int = 0

    def __init__(self):
        Room.total_rooms += 1
        self.room_number: int = Room.total_rooms
        self.sides: Dict[str, Side] = {
            'north': None,
            'east': None,
            'south': None,
            'west': None
        }

    def enter(self) -> None:
        pass
    def get_side(self, direction: str) -> Side:
        return self.sides[direction]
    
    def set_side(self, direction: str, side: Side) -> None:
        self.sides[direction] = side
    
    def __repr__(self):
        payload: str = f'Room({self.room_number}, {repr(self.sides)})'
        return payload