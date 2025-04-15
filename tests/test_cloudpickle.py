import cloudpickle
import inspect
import typing
from numeus.cloudpickle.file import (
    basic,
    annotated,
    annotated_builder,
    default_builder,
)


def test_cloudpickle_basic() -> None:
    assert basic() == 1

    pickled_obj = cloudpickle.loads(cloudpickle.dumps(basic))
    assert pickled_obj() == 1


def test_cloudpickle_annotations() -> None:
    signature = inspect.signature(annotated)
    annotations = typing.get_type_hints(annotated)

    pickled_obj = cloudpickle.loads(cloudpickle.dumps(annotated))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations


def test_cloudpickle_nested_annotations() -> None:
    nested = annotated_builder()
    signature = inspect.signature(nested)
    annotations = typing.get_type_hints(nested)

    pickled_obj = cloudpickle.loads(cloudpickle.dumps(nested))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations


def test_cloudpickle_defaults() -> None:
    nested = default_builder()
    assert nested() == 3
    assert nested.__defaults__ == (1, 2)

    pickled_obj = cloudpickle.loads(cloudpickle.dumps(nested))
    # unknown opcode
    assert pickled_obj() == 3
    assert pickled_obj.__defaults__ == (1, 2)
