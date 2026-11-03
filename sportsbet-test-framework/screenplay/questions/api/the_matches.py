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
        self.only_upcoming = False

    def upcoming(self) -> TheMatches:
        self.only_upcoming = True
        return self

    def __str__(self) -> str:
        return "the upcoming matches" if self.only_upcoming else "the matches"

    def answered_by(self, actor: Actor) -> list[dict[str, Any]]:
        response = actor.ability_to(CallAnApi).send(HTTPMethod.GET, Endpoints.MATCHES)
        response.raise_for_status()
        matches = response.json()
        if self.only_upcoming:
            today = date.today().isoformat()
            matches = [match for match in matches if match["kickoffDate"] >= today]
        return matches
