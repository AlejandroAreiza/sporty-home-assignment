from screenplay.abilities import BrowseTheWeb
from screenplay.actor import Actor
from screenplay.interfaces import Question


class ThePageTitle(Question):
    def __str__(self) -> str:
        return "the page title"

    def answered_by(self, actor: Actor) -> str:
        return actor.ability_to(BrowseTheWeb).driver.title
