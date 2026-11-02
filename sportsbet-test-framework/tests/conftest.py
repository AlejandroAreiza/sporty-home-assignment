import pytest
from allure import step
from selenium.webdriver import Chrome

from config.settings import EnvVariables
from screenplay.abilities import CallAnApi
from screenplay.actor import Actor
from screenplay.pages.sportbet_page import SportBetPage

QA_BASE_URL = EnvVariables.QA_BASE_URL
QA_USER_ID = EnvVariables.QA_USER_ID


@pytest.fixture(scope="session")
def driver():
    with step("Initiate Chrome driver"):
        _driver = Chrome()
        _driver.maximize_window()
    yield _driver
    with step("Quit Chrome driver"):
        _driver.quit()


@pytest.fixture
def sportbet_page(driver):
    with step(f"Open sportsbet page as '{QA_USER_ID}'"):
        return SportBetPage(driver).open().login_as(QA_USER_ID)


@pytest.fixture
def api_user():
    with step("Create actor 'Api User'"):
        actor = Actor.named("Api User").who_can(
            CallAnApi.at(QA_BASE_URL, {"x-user-id": QA_USER_ID})
        )
    yield actor
    actor.exit()
