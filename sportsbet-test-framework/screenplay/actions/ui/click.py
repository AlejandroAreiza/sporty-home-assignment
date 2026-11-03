from __future__ import annotations

from screenplay.abilities import BrowseTheWeb
from screenplay.actor import Actor
from screenplay.interfaces import Performable
from screenplay.ui import UIElement


class Click(Performable):
    def __init__(self, element: UIElement) -> None:
        self.element = element

    @classmethod
    def on(cls, element: UIElement) -> Click:
        return cls(element)

    def __str__(self) -> str:
        return f"click on {self.element}"

    def perform(self, actor: Actor) -> None:
        actor.ability_to(BrowseTheWeb).find_clickable(self.element).click()
