from http import HTTPMethod
from typing import Any

from config.endpoints import Endpoints
from screenplay.abilities import CallAnApi
from screenplay.actor import Actor
from screenplay.interfaces import Question


class TheBalance(Question):
    def __str__(self) -> str:
        return "the balance in the API"

    def answered_by(self, actor: Actor) -> Any:
        response = actor.ability_to(CallAnApi).send(HTTPMethod.GET, Endpoints.BALANCE)
        response.raise_for_status()
        return response.json()
