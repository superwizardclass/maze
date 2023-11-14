from abc import ABC, abstractmethod

class Side(ABC):
    @abstractmethod
    def enter(self) -> None:
        pass
