from enum import StrEnum


class Selection(StrEnum):
    HOME = "HOME"
    DRAW = "DRAW"
    AWAY = "AWAY"

    @property
    def key(self) -> str:
        return self.value.lower()

    @property
    def label(self) -> str:
        return self.value.title()
