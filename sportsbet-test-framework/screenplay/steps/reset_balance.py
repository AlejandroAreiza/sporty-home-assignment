import requests

from config.endpoints import Endpoints
from screenplay.actions import Post
from screenplay.actor import Actor
from screenplay.interfaces import Performable


class ResetBalance(Performable):
    def __str__(self) -> str:
        return "reset the balance"

    def perform(self, actor: Actor) -> requests.Response:
        return actor.attempts_to(Post.to(Endpoints.RESET_BALANCE))
