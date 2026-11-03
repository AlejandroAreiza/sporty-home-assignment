import pytest

from screenplay.questions.ui import ThePageTitle


class TestSmoke:
    @pytest.mark.smoke
    def test_open_the_app_should_show_the_title(self, player):
        player.asserts(ThePageTitle(), "Sports Betting QA")
