if __name__ == '__main__':
    from maze_manager import MazeManager
    from maze import Maze
    from explorer import Explorer

    maze_manager: MazeManager = MazeManager()
    maze_game: Maze = maze_manager.create_maze()

    explorer: Explorer = Explorer()
    