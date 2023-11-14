from side import Side

class Door(Side):
    def __init__(self, is_open, r1, r2):
        self.is_open = is_open
        self.r1 = r1
        self.r2 = r2

    def enter():
        pass

    def __repr__(self):
        payload: str = f'Door({self.is_open}, {self.r1.room_number}, {self.r2.room_number})'
        return payload