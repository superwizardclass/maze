if __name__ == '__main__':
    import hello
    from state_manager import StateManager
    from maze import Maze
    from player import Player


    state_manager: StateManager = StateManager()
    maze: Maze = state_manager.create_maze()
    player: Player = state_manager.create_player()

    hello.hello()