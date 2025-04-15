from typing import Any


def basic() -> int:
    return 1


def annotated(a: str, b: int) -> float:
    return 1.5


def annotated_builder() -> Any:
    def nested(a: str, b: int) -> float:
        return 1.5

    return nested


def default_builder() -> Any:
    def nested(a: int = 1, b: int = 2) -> int:
        return a + b

    return nested
