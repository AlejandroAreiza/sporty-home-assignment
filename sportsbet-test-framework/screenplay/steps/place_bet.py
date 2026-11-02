from __future__ import annotations

import requests

from config.endpoints import Endpoints
from screenplay.actions import Post
from screenplay.actor import Actor
from screenplay.interfaces import Performable
from screenplay.models import Selection


class PlaceBet(Performable):
    def __init__(self) -> None:
        self.match_id: str | None = None
        self.selection: Selection = Selection.HOME
        self.stake: float | None = None

    def with_match_id(self, match_id: str) -> PlaceBet:
        self.match_id = match_id
        return self

    def with_selection(self, selection: Selection) -> PlaceBet:
        self.selection = selection
        return self

    def with_stake(self, stake: float) -> PlaceBet:
        self.stake = stake
        return self

    def __str__(self) -> str:
        return f"place a bet of {self.stake} on {self.selection} for {self.match_id}"

    def perform(self, actor: Actor) -> requests.Response:
        body = {"matchId": self.match_id, "selection": self.selection, "stake": self.stake}
        return actor.attempts_to(Post.to(Endpoints.PLACE_BET).with_body(body))
