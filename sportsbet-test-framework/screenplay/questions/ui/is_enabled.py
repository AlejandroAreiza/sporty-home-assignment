from __future__ import annotations

from screenplay.abilities import BrowseTheWeb
from screenplay.actor import Actor
from screenplay.interfaces import Question
from screenplay.ui import UIElement


class IsEnabled(Question):
    def __init__(self, element: UIElement) -> None:
        self.element = element

    @classmethod
    def the(cls, element: UIElement) -> IsEnabled:
        return cls(element)

    def __str__(self) -> str:
        return f"whether {self.element} is enabled"

    def answered_by(self, actor: Actor) -> bool:
        return actor.ability_to(BrowseTheWeb).find(self.element).is_enabled()
