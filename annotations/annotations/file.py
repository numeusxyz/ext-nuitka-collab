from typing import Any


def annotated(a: str, b: int) -> float:
    return 1.5


def builder() -> Any:
    def nested(a: str, b: int) -> float:
        return 1.5

    return nested
