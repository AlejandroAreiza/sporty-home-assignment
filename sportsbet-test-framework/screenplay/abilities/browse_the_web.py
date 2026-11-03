from __future__ import annotations

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from screenplay.interfaces import Ability
from screenplay.ui.ui_element import UIElement


class BrowseTheWeb(Ability):
    def __init__(
        self, driver: WebDriver, base_url: str, timeout: float = 10, polling: float = 0.2
    ) -> None:
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(
            driver,
            timeout,
            poll_frequency=polling,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        )

    @classmethod
    def using(cls, driver: WebDriver, base_url: str) -> BrowseTheWeb:
        return cls(driver, base_url)

    def open(self, path: str = "/") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def find(self, element: UIElement) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(element.locator))

    def find_clickable(self, element: UIElement) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(element.locator))

    def forget(self) -> None:
        self.driver.delete_all_cookies()
