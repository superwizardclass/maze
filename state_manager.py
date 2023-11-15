from maze import Maze
from room import Room
from door import Door
from wall import Wall
from player import Player
from explorer import Explorer

class StateManager:
    def __init__(self):
        pass
    
    def create_maze(self) -> Maze:
        m1: Maze = Maze()
        r1: Room = Room()
        r2: Room = Room()
        d1_2: Door = Door(False, r1, r2)

        m1.add_room(r1)
        m1.add_room(r2)

        r1.set_side('north', Wall())
        r1.set_side('east',d1_2)
        r1.set_side('south', Wall())
        r1.set_side('west', Wall())

        r2.set_side('north', Wall())
        r2.set_side('east', Wall())
        r2.set_side('south', Wall())
        r2.set_side('west', d1_2)

        return m1

    def create_player(self) -> Player:
        p1: Player = Explorer()
        return p1