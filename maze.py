from room import Room

class Maze():
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def find_room(self, room_number) -> bool:
        pass

    def __repr__(self):
        payload: str = f'Maze({repr(self.rooms)})'
        return payload