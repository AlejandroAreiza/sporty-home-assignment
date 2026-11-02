from __future__ import annotations

from http import HTTPMethod

import requests

from screenplay.interfaces import Ability


class CallAnApi(Ability):
    def __init__(self, base_url: str, session: requests.Session):
        self.base_url = base_url
        self.session = session

    @classmethod
    def at(cls, base_url: str, headers: dict[str, str]) -> CallAnApi:
        session = requests.Session()
        session.headers.update(headers)
        return cls(base_url, session)

    def send(self, method: HTTPMethod, path: str, **kwargs) -> requests.Response:
        return self.session.request(method, f"{self.base_url}{path}", timeout=10, **kwargs)

    def forget(self) -> None:
        self.session.close()
