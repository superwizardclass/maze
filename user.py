from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def move(self) -> None:
        pass