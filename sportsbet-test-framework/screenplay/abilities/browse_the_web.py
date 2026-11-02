from selenium.webdriver import Chrome

from screenplay.interfaces import Ability


class BrowseTheWeb(Ability):
    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def ready_state(self) -> str:
        return self.driver.execute_script("return document.readyState")

    def __init__(self):
        self.driver = Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

    def open(self, base_url: str) -> BrowseTheWeb:
        self.base_url = base_url
        self.driver.get(self.base_url)
        return self

    def login_as(self, user_id: str) -> BrowseTheWeb:
        self.driver.get(f"{self.base_url}/?user-id={user_id}")
        return self

    def forget(self) -> None:
        self.driver.quit()
