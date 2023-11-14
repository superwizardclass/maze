from side import Side

class Room(Side):
    def __init__(self):
        self.room_number: int = 0
        self.sides = {
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