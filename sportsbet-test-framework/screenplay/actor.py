from __future__ import annotations

from typing import Any, cast

import allure

from screenplay.interfaces import Ability, Performable, Question


class Actor:
    def __init__(self, name: str) -> None:
        self.name = name
        self.abilities: dict[type[Ability], Ability] = {}

    @classmethod
    def named(cls, name: str) -> Actor:
        return cls(name)

    def who_can(self, *abilities: Ability) -> Actor:
        for ability in abilities:
            self.abilities[type(ability)] = ability
        return self

    def ability_to[A: Ability](self, ability_class: type[A]) -> A:
        try:
            return cast(A, self.abilities[ability_class])
        except KeyError:
            raise RuntimeError(
                f"{self.name} does not have the ability {ability_class.__name__}"
            ) from None

    def attempts_to(self, *performables: Performable) -> Any:
        """Performs each step or action and returns the result of the last one."""
        result = None
        for performable in performables:
            with allure.step(f"{self.name} attempts to {performable}"):
                result = performable.perform(self)
        return result

    def asks_for(self, question: Question) -> Any:
        with allure.step(f"{self.name} asks for {question}"):
            return question.answered_by(self)

    def verifies(self, actual: Question | Any, expected: Any) -> None:
        """Checks a question's answer, or a value you already have, against the expected value."""
        with allure.step(f"{self.name} verifies {actual} is {expected}"):
            if isinstance(actual, Question):
                actual = self.asks_for(actual)
            assert actual == expected, f"{self.name} expected {expected}, got {actual}"

    def exit(self) -> None:
        for ability in self.abilities.values():
            ability.forget()
