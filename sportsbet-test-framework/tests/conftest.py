import pytest
from allure import step
from selenium.webdriver import Chrome, ChromeOptions

from config.settings import EnvVariables
from screenplay.abilities import BrowseTheWeb, CallAnApi
from screenplay.actions.ui import OpenWebPage
from screenplay.actor import Actor
from screenplay.steps.api import ResetBalance

QA_BASE_URL = EnvVariables.QA_BASE_URL
QA_USER_ID = EnvVariables.QA_USER_ID


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="run without a window")


@pytest.fixture(scope="session")
def driver(request):
    options = ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,900")
    with step("Initiate Chrome driver"):
        browser = Chrome(options=options)
        browser.maximize_window()
    yield browser
    with step("Quit Chrome driver"):
        browser.quit()


@pytest.fixture
def api_player():
    with step("Create actor 'Api Player' with ability to CallAnApi"):
        actor = Actor.named("Api Player").who_can(
            CallAnApi.at(QA_BASE_URL, {"x-user-id": QA_USER_ID})
        )
    yield actor
    actor.exit()


@pytest.fixture
def player(driver):
    with step("Create actor 'Player' with ability to BrowseTheWeb and CallAnApi"):
        actor = Actor.named("Player").who_can(
            BrowseTheWeb.using(driver, QA_BASE_URL),
            CallAnApi.at(QA_BASE_URL, {"x-user-id": QA_USER_ID}),
        )
    with step("Reset the balance and open the app as the player"):
        actor.attempts_to(ResetBalance(), OpenWebPage.as_user(QA_USER_ID))
    yield actor
    actor.exit()


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item: pytest.Function):
    try:
        return (yield)
    finally:
        for value in item.funcargs.values():
            if isinstance(value, Actor):
                value.raise_failures()
