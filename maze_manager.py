from maze import Maze
from room import Room
from door import Door


class MazeManager:
    def create_maze() -> Maze:
        m1: Maze = Maze()
        r1: Room = Room()
        r2: Room = Room()
        d1: Door = Door()

        m1.add_room(r1)
        m1.add_room(r2)

        return m1
