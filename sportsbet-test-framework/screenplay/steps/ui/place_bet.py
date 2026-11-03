from __future__ import annotations

from screenplay.actions.ui import Click, Enter
from screenplay.actor import Actor
from screenplay.interfaces import Performable
from screenplay.models import Selection
from screenplay.ui import BetSlip, MatchList


class PlaceBet(Performable):
    def __init__(self) -> None:
        self.match_id: str | None = None
        self.actions: list[Performable] = []

    def on_match(self, match_id: str) -> PlaceBet:
        self.match_id = match_id
        return self

    def with_selection(self, selection: Selection) -> PlaceBet:
        if self.match_id is None:
            raise ValueError("PlaceBet needs a match first: use .on_match(match_id)")
        self.actions.append(Click.on(MatchList.match(self.match_id).odds(selection)))
        return self

    def with_stake(self, stake: float) -> PlaceBet:
        self.actions.append(Enter.the_value(f"{stake:.2f}").into(BetSlip.STAKE))
        return self

    def confirm(self) -> PlaceBet:
        self.actions.append(Click.on(BetSlip.PLACE_BET_BUTTON))
        return self

    def __str__(self) -> str:
        return "place a bet"

    def perform(self, actor: Actor) -> None:
        for action in self.actions:
            actor.attempts_to(action)
