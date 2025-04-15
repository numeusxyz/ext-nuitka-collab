import dill
from defaults.file import builder


def test_defaults() -> None:
    defaults = builder()
    assert defaults() == 3
    assert defaults.__defaults__ == (1, 2)

    pickled_obj = dill.loads(dill.dumps(defaults))
    # segfaults
    assert pickled_obj() == 3
    assert pickled_obj.__defaults__ == (1, 2)
