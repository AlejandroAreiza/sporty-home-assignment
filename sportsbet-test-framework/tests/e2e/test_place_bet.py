import pytest

from screenplay.actions.ui import Click
from screenplay.models import Selection
from screenplay.questions.api import TheBalance, TheMatches
from screenplay.questions.ui import IsEnabled, TheText
from screenplay.steps.ui import PlaceBet
from screenplay.ui import BetSlip, Header, Receipt


class TestPlaceBet:
    """TC-01: a user can place a valid single bet on an upcoming match through the UI.
    Why this test: It is the core money flow and the main user journey.
    It checks every step a user sees (bet slip, stake, Place Bet, receipt, balance),
    so one test protects the most business value. It catches 3 Critical/High bugs.
    """

    @pytest.mark.regression
    @pytest.mark.ui
    def test_place_a_valid_single_bet_on_an_upcoming_match(self, player):
        stake = 100.00
        selection = Selection.HOME
        balance = player.asks_for(TheBalance())["balance"]
        match = player.asks_for(TheMatches().upcoming())[0]
        odds = match["odds"][selection.key]
        match_name = f"{match['homeTeam']} vs {match['awayTeam']}"
        selection_label = f"Match Winner: {selection.label}"
        payout = f"€{stake * odds:.2f}"

        player.asserts_soft(TheText.of(Header.BALANCE), f"Balance: €{balance:.2f}")

        player.attempts_to(PlaceBet().on_match(match["id"]).with_selection(selection))
        player.asserts_soft(TheText.of(BetSlip.MATCH), match_name)
        player.asserts_soft(TheText.of(BetSlip.SELECTION), selection_label)
        player.asserts_soft(TheText.of(BetSlip.ODDS), f"Odds: {odds:.2f}")
        player.asserts_soft(TheText.of(BetSlip.SELECTION_COUNT), "1")
        player.asserts_soft(IsEnabled.the(BetSlip.PLACE_BET_BUTTON), False)

        player.attempts_to(PlaceBet().with_stake(stake))
        player.asserts(IsEnabled.the(BetSlip.PLACE_BET_BUTTON), True)
        player.asserts(TheText.of(BetSlip.TOTAL_STAKE), f"€{stake:.2f}")
        player.asserts(TheText.of(BetSlip.POTENTIAL_PAYOUT), payout)

        player.attempts_to(PlaceBet().confirm())
        player.asserts_soft(TheText.of(BetSlip.PLACE_BET_BUTTON), "PLACING...")
        player.asserts_soft(TheText.of(Receipt.MATCH), match_name)
        player.asserts_soft(TheText.of(Receipt.STAKE), f"€{stake:.2f}")
        player.asserts_soft(TheText.of(Receipt.ODDS), f"{odds:.2f}")
        player.asserts_soft(TheText.of(Receipt.PAYOUT), payout)

        player.attempts_to(Click.on(Receipt.CLOSE))
        player.asserts_soft(TheText.of(BetSlip.SELECTION_COUNT), "0")
        player.asserts_soft(TheText.of(Header.BALANCE), f"Balance: €{balance - stake:.2f}")
