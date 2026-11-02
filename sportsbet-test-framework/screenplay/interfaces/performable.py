from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from screenplay.actor import Actor


class Performable(ABC):
    @abstractmethod
    def perform(self, actor: Actor) -> Any: ...

    def __str__(self) -> str:
        return type(self).__name__
