from http import HTTPStatus

import pytest

from screenplay.steps.api import ResetBalance


class TestSmoke:
    @pytest.mark.smoke
    @pytest.mark.api
    def test_reset_the_balance_should_return_ok(self, api_player):
        response = api_player.attempts_to(ResetBalance())
        api_player.asserts(response.status_code, HTTPStatus.OK)
