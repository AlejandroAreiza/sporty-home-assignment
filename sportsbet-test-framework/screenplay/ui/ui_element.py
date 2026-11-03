from __future__ import annotations

from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass(frozen=True)
class UIElement:
    name: str
    by: str
    value: str

    @classmethod
    def by_id(cls, name: str, element_id: str) -> UIElement:
        return cls(name, By.ID, element_id)

    @classmethod
    def by_css(cls, name: str, css: str) -> UIElement:
        return cls(name, By.CSS_SELECTOR, css)

    @classmethod
    def by_xpath(cls, name: str, xpath: str) -> UIElement:
        return cls(name, By.XPATH, xpath)

    @property
    def locator(self) -> tuple[str, str]:
        return (self.by, self.value)

    def __str__(self) -> str:
        return self.name
