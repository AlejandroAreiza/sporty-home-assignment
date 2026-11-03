from __future__ import annotations

from screenplay.models import Selection
from screenplay.ui.ui_element import UIElement


class MatchCard:
    def __init__(self, match_id: str) -> None:
        self.match_id = match_id

    def odds(self, selection: Selection) -> UIElement:
        return UIElement.by_id(
            f"the {selection} odds of {self.match_id}",
            f"odds-{self.match_id}-{selection.key}",
        )


class MatchList:
    @staticmethod
    def match(match_id: str) -> MatchCard:
        return MatchCard(match_id)
