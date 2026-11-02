from http import HTTPStatus

import pytest

from screenplay.questions import TheBalance
from screenplay.steps import ResetBalance


class TestResetBalance:

    @pytest.mark.smoke
    def test_reset_the_balance_should_return_ok(self, api_user):
        response = api_user.attempts_to(ResetBalance())
        api_user.verifies(response.status_code, HTTPStatus.OK)
