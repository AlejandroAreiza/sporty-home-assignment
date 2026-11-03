from __future__ import annotations

from screenplay.abilities import BrowseTheWeb
from screenplay.actor import Actor
from screenplay.interfaces import Performable
from screenplay.ui import UIElement


class Enter(Performable):
    def __init__(self, value: str) -> None:
        self.value = value
        self.element: UIElement | None = None

    @classmethod
    def the_value(cls, value: str) -> Enter:
        return cls(value)

    def into(self, element: UIElement) -> Enter:
        self.element = element
        return self

    def __str__(self) -> str:
        return f"enter {self.value} into {self.element or '?'}"

    def perform(self, actor: Actor) -> None:
        if self.element is None:
            raise ValueError("Enter needs an element")
        field = actor.ability_to(BrowseTheWeb).find(self.element)
        field.clear()
        field.send_keys(self.value)
