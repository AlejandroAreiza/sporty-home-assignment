from __future__ import annotations

from http import HTTPMethod

import requests

from screenplay.interfaces import Ability


class CallAnApi(Ability):
    def __init__(self, base_url: str, session: requests.Session):
        self.base_url = base_url
        self.session = session
        self.last_response: requests.Response | None = None

    @classmethod
    def at(cls, base_url: str, headers: dict[str, str]) -> CallAnApi:
        session = requests.Session()
        session.headers.update(headers)
        return cls(base_url, session)

    def send(self, method: HTTPMethod, path: str, **kwargs) -> requests.Response:
        self.last_response = self.session.request(
            method, f"{self.base_url}{path}", timeout=10, **kwargs
        )
        return self.last_response

    def forget(self) -> None:
        self.session.close()
