
import cloudpickle, inspect, typing

def f():
    def annotated(a: str, b: int) -> int:
        pass

    return annotated

annotated = f()

def test_cloudpickle_annotations():
    signature = inspect.signature(annotated)
    annotations = typing.get_type_hints(annotated)

    pickled_obj = cloudpickle.loads(cloudpickle.dumps(annotated))
    pickled_signature = inspect.signature(pickled_obj)
    pickled_annotations = typing.get_type_hints(pickled_obj)

    assert signature == pickled_signature
    assert annotations == pickled_annotations

    print(pickled_annotations)

test_cloudpickle_annotations()

print("compiled" if "__compiled__" in globals() else "uncompiled")