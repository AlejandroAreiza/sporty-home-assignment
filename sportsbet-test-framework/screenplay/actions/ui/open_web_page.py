from __future__ import annotations

from screenplay.abilities import BrowseTheWeb
from screenplay.actor import Actor
from screenplay.interfaces import Performable


class OpenWebPage(Performable):
    def __init__(self, path: str) -> None:
        self.path = path

    @classmethod
    def as_user(cls, user_id: str) -> OpenWebPage:
        return cls(f"/?user-id={user_id}")

    def __str__(self) -> str:
        return f"open the web page {self.path}"

    def perform(self, actor: Actor) -> None:
        actor.ability_to(BrowseTheWeb).open(self.path)
