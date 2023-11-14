from side import Side

class Wall(Side):

    def enter(self) -> None:
        pass

    def __repr__(self):
        payload: str = f'Wall()'
        return payload 