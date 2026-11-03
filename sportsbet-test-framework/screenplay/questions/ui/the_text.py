from __future__ import annotations

from screenplay.abilities import BrowseTheWeb
from screenplay.actor import Actor
from screenplay.interfaces import Question
from screenplay.ui import UIElement


class TheText(Question):
    def __init__(self, element: UIElement) -> None:
        self.element = element

    @classmethod
    def of(cls, element: UIElement) -> TheText:
        return cls(element)

    def __str__(self) -> str:
        return f"the text of {self.element}"

    def answered_by(self, actor: Actor) -> str:
        return actor.ability_to(BrowseTheWeb).find(self.element).text
