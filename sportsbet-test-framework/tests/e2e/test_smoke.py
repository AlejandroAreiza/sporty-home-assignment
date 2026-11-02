import pytest
from allure import step


class TestSmoke:
    WEBAPP_TITLE = "Sports Betting QA"

    @pytest.mark.smoke
    def test_open_sportbet_page_should_succeed(self, sportbet_page):
        with step("Verify sportbet page opened successfully"):
            with step("Verify sportbet page is in ready state"):
                assert sportbet_page.ready_state == "complete"
            with step(f"Verify sportbet page title contains: '{self.WEBAPP_TITLE}'"):
                assert sportbet_page.title == self.WEBAPP_TITLE
