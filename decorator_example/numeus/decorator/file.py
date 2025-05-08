def decorator(func):
    def wrapper():
        return func

    return wrapper


@decorator
def my_function():
    ...
