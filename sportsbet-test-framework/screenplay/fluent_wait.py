import time
from collections.abc import Callable


class FluentWait:
    def __init__(self, timeout: float = 2, polling: float = 0.2) -> None:
        self.timeout = timeout
        self.polling = polling

    def until[T](self, action: Callable[[], T], condition: Callable[[T], bool]) -> T:
        deadline = time.monotonic() + self.timeout
        result = action()
        while not condition(result) and time.monotonic() < deadline:
            time.sleep(self.polling)
            result = action()
        return result
