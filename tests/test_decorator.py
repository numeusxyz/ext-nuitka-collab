import pytest
import cloudpickle
import ray.cloudpickle
from numeus.decorator.file import my_function


@pytest.mark.parametrize('pickler', [cloudpickle, ray.cloudpickle])
def test_decorator(pickler):
    for i in range(100000):
        if i % 100 == 0:
            print(i)

        pickler.dumps(my_function, protocol=5)
