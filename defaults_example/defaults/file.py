from typing import Any


def builder() -> Any:
    def func(a: int = 1, b: int = 2) -> int:
        return a + b

    return func
