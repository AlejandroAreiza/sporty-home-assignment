from http import HTTPStatus

import pytest

from screenplay.steps import ResetBalance


class TestSmoke:
    @pytest.mark.smoke
    def test_reset_the_balance_should_return_ok(self, api_user):
        response = api_user.attempts_to(ResetBalance())
        api_user.asserts(response.status_code, HTTPStatus.OK)
