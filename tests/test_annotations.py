import dill
import inspect
import typing
from annotations.file import annotated, builder


def test_annotations() -> None:
    signature = inspect.signature(annotated)
    annotations = typing.get_type_hints(annotated)

    pickled_obj = dill.loads(dill.dumps(annotated))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations


def test_nested_annotations() -> None:
    nested = builder()
    signature = inspect.signature(nested)
    annotations = typing.get_type_hints(nested)

    pickled_obj = dill.loads(dill.dumps(nested))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations
