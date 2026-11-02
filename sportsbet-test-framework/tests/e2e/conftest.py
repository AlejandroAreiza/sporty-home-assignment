import os
from pathlib import Path

import pytest
from allure import step
from dotenv import load_dotenv
from selenium.webdriver import Chrome

from screenplay.pages.sportbet_page import SportBetPage

load_dotenv(Path(__file__).parents[2] / ".env")

QA_USER_ID = os.environ["QA_USER_ID"]


@pytest.fixture(scope="session", autouse=True)
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