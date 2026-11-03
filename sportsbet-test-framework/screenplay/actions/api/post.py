from __future__ import annotations

from http import HTTPMethod
from typing import Any

import requests

from screenplay.abilities import CallAnApi
from screenplay.actor import Actor
from screenplay.interfaces import Performable


class Post(Performable):
    def __init__(self, path: str) -> None:
        self.path = path
        self.body: dict[str, Any] | None = None

    @classmethod
    def to(cls, path: str) -> Post:
        return cls(path)

    def with_body(self, body: dict[str, Any]) -> Post:
        self.body = body
        return self

    def __str__(self) -> str:
        return f"POST {self.path}"

    def perform(self, actor: Actor) -> requests.Response:
        return actor.ability_to(CallAnApi).send(HTTPMethod.POST, self.path, json=self.body)
