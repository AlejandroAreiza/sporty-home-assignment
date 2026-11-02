import os
from pathlib import Path

from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver

load_dotenv(Path(__file__).parents[2] / ".env")


class SportBetPage:
    BASE_URL = os.environ["QA_BASE_URL"]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> SportBetPage:
        self.driver.delete_all_cookies()
        self.driver.get(self.BASE_URL)
        return self

    def login_as(self, user_id: str) -> SportBetPage:
        self.driver.get(f"{self.BASE_URL}/?user-id={user_id}")
        return self

    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def ready_state(self) -> str:
        return self.driver.execute_script("return document.readyState")
