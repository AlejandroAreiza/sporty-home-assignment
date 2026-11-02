from http import HTTPStatus

import pytest

from screenplay.models import Selection
from screenplay.questions import TheBalance, TheMatches
from screenplay.steps import PlaceBet, ResetBalance


class TestPlaceBet:
    """TC-02: the API must enforce the €100.00 maximum stake.
    Why this test: a stake above the maximum creates a large, unplanned payout risk,
    and only a direct API call proves the backend enforces the limit (the UI can be
    bypassed). Equivalence Partitioning + Boundary Value Analysis: 100.00 (edge of the
    valid range) is accepted, 100.01 (edge of the above-maximum range) is rejected.
    """

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "stake, expected_status, expected_payload",
        [
            pytest.param(
                100.00,
                HTTPStatus.OK,
                {
                    "message": "Bet placed successfully",
                    "stake": 100.00,
                    "currency": "EUR",
                },
                id="at-max",
            ),
            pytest.param(
                100.01,
                HTTPStatus.UNPROCESSABLE_CONTENT,
                {
                    "error": "invalid_stake_max",
                    "message": "Stake must be at most 100.00.",
                },
                id="above-max",
            ),
        ],
    )
    def test_verify_the_api_enforces_the_maximum_stake(
        self, api_user, stake, expected_status, expected_payload
    ):

        api_user.attempts_to(ResetBalance())
        initial_balance = api_user.asks_for(TheBalance())["balance"]
        match = api_user.asks_for(TheMatches().upcoming().first())
        selection = Selection.DRAW

        response = api_user.attempts_to(
            PlaceBet().with_match_id(match["id"]).with_selection(selection).with_stake(stake)
        )
        succeedBet = expected_status == HTTPStatus.OK
        if succeedBet:
            odds = match["odds"][selection.value.lower()]
            expected_payload = {
                **expected_payload,
                "matchId": match["id"],
                "selection": selection.value,
                "odds": odds,
                "payout": round(stake * odds, 2),
                "balance": initial_balance - stake,
            }

        api_user.asserts(response.status_code, expected_status)

        api_user.asserts(
            {key: response.json().get(key) for key in expected_payload},
            expected_payload,
        )

        expected_balance = initial_balance - stake if succeedBet else initial_balance
        api_user.asserts(TheBalance(), {"balance": expected_balance, "currency": "EUR"})
