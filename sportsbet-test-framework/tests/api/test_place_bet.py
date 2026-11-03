from http import HTTPStatus

import pytest

from screenplay.models import Selection
from screenplay.questions.api import TheBalance, TheMatches
from screenplay.steps.api import PlaceBet, ResetBalance


class TestPlaceBet:
    """TC-02: the API must enforce the €100.00 maximum stake.
    Why this test: a stake above the maximum creates a large, unplanned payout risk,
    and only a direct API call proves the backend enforces the limit (the UI can be
    bypassed). Equivalence Partitioning + Boundary Value Analysis: 100.00 (edge of the
    valid range) is accepted, 100.01 (edge of the above-maximum range) is rejected.
    """

    @pytest.mark.regression
    @pytest.mark.api
    @pytest.mark.parametrize(
        "stake, expected_status, expected_payload",
        [
            pytest.param(
                100.00,
                HTTPStatus.OK,
                {"message": "Bet placed successfully", "stake": 100.00, "currency": "EUR"},
                id="at-max",
            ),
            pytest.param(
                100.01,
                HTTPStatus.UNPROCESSABLE_CONTENT,
                {"error": "invalid_stake_max", "message": "Stake must be at most 100.00."},
                id="above-max",
            ),
        ],
    )
    def test_verify_the_api_enforces_the_maximum_stake(
        self, api_player, stake, expected_status, expected_payload
    ):
        # arrange
        selection = Selection.DRAW
        api_player.attempts_to(ResetBalance())
        balance = api_player.asks_for(TheBalance())["balance"]
        match = api_player.asks_for(TheMatches().upcoming())[0]
        succeed = expected_status == HTTPStatus.OK

        # act
        response = api_player.attempts_to(
            PlaceBet().on_match(match["id"]).with_selection(selection).with_stake(stake)
        )

        # assert
        if succeed:
            odds = match["odds"][selection.key]
            balance -= stake
            expected_payload = expected_payload | {
                "matchId": match["id"],
                "selection": selection.value,
                "odds": odds,
                "payout": round(stake * odds, 2),
                "balance": balance,
            }
        api_player.asserts(response.status_code, expected_status)
        api_player.asserts_soft(response.json(), expected_payload)
        api_player.asserts_soft(TheBalance(), {"balance": balance, "currency": "EUR"})
