import cloudpickle
import inspect
import pytest
import ray
import typing
from numeus.cloudpickle.file import (
    basic,
    annotated,
    annotated_builder,
    default_builder,
)


@pytest.mark.parametrize('pickler', [cloudpickle, ray.cloudpickle])
def test_cloudpickle_basic(pickler) -> None:
    assert basic() == 1

    pickled_obj = pickler.loads(pickler.dumps(basic))
    assert pickled_obj() == 1


@pytest.mark.parametrize('pickler', [cloudpickle, ray.cloudpickle])
def test_cloudpickle_annotations(pickler) -> None:
    signature = inspect.signature(annotated)
    annotations = typing.get_type_hints(annotated)

    pickled_obj = pickler.loads(pickler.dumps(annotated))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations


@pytest.mark.parametrize('pickler', [cloudpickle, ray.cloudpickle])
def test_cloudpickle_nested_annotations(pickler) -> None:
    nested = annotated_builder()
    signature = inspect.signature(nested)
    annotations = typing.get_type_hints(nested)

    pickled_obj = pickler.loads(pickler.dumps(nested))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations


@pytest.mark.parametrize('pickler', [cloudpickle, ray.cloudpickle])
def test_cloudpickle_defaults(pickler) -> None:
    nested = default_builder()
    assert nested() == 3
    assert nested.__defaults__ == (1, 2)

    pickled_obj = pickler.loads(pickler.dumps(nested))
    # unknown opcode
    assert pickled_obj() == 3
    assert pickled_obj.__defaults__ == (1, 2)
