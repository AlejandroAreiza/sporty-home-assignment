from __future__ import annotations

from datetime import date
from http import HTTPMethod
from typing import Any

from config.endpoints import Endpoints
from screenplay.abilities import CallAnApi
from screenplay.actor import Actor
from screenplay.interfaces import Question


class TheMatches(Question):
    def __init__(self) -> None:
        self.predicate = lambda match: True
        self.only_first = False

    def upcoming(self) -> TheMatches:
        today = date.today().isoformat()
        self.predicate = lambda match: match["kickoffDate"] >= today
        return self

    def first(self) -> TheMatches:
        self.only_first = True
        return self

    def __str__(self) -> str:
        return "the matches"

    def answered_by(self, actor: Actor) -> Any:
        response = actor.ability_to(CallAnApi).send(HTTPMethod.GET, Endpoints.MATCHES)
        response.raise_for_status()
        matches = [match for match in response.json() if self.predicate(match)]
        return matches[0] if self.only_first else matches
