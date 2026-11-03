from __future__ import annotations

from typing import Any, cast

import allure

from screenplay.fluent_wait import FluentWait
from screenplay.interfaces import Ability, Performable, Question


class Actor:
    def __init__(self, name: str) -> None:
        self.name = name
        self.abilities: dict[type[Ability], Ability] = {}
        self.failures: list[str] = []

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
        result = None
        for performable in performables:
            with allure.step(f"{self.name} attempts to {performable}"):
                result = performable.perform(self)
        return result

    def asks_for(self, question: Question) -> Any:
        with allure.step(f"{self.name} asks for {question}"):
            return question.answered_by(self)

    def asserts(self, actual: Question | Any, expected: Any) -> None:
        try:
            self._compare("asserts", actual, expected)
        except AssertionError as error:
            self.failures.append(f"hard: {error}")
            raise

    def asserts_soft(self, actual: Question | Any, expected: Any) -> None:
        try:
            self._compare("asserts soft", actual, expected)
        except AssertionError as error:
            self.failures.append(f"soft: {error}")

    def raise_failures(self) -> None:
        if self.failures:
            details = "\n".join(f"- {failure}" for failure in self.failures)
            noun = "assert" if len(self.failures) == 1 else "asserts"
            raise AssertionError(f"{len(self.failures)} {noun} failed:\n{details}")

    def _compare(self, verb: str, actual: Question | Any, expected: Any) -> None:
        with allure.step(f"{self.name} {verb} {actual} is {expected}"):
            if isinstance(actual, Question):  # ← this line comes back
                actual = FluentWait().until(
                    action=lambda: actual.answered_by(self),
                    condition=lambda answer: answer == expected,
                )
            assert actual == expected, f"{actual} is not {expected}"

    def exit(self) -> None:
        for ability in self.abilities.values():
            ability.forget()
