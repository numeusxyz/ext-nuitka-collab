import cloudpickle


def decorator(func):
    def wrapper():
        return func

    return wrapper


@decorator
def my_function():
    ...


for i in range(10000):
    print(i)

    cloudpickle.dumps(my_function, protocol=5)
