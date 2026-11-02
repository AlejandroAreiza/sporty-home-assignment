from abc import ABC, abstractmethod


class Ability(ABC):
    @abstractmethod
    def forget(self) -> None: ...
