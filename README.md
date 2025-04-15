# Nuitka Collab

### Initial Setup

```shell
# using uv
uv venv --python 3.10
source .venv/bin/activate
uv pip install -r requirements.txt

# using Python/pip
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After the initial setup, the environment can be updated with
```shell
uv pip install -r requirements.txt --reinstall
# or
pip install -r requirements.txt --force-reinstall
````

### annotations

This folder contains a simple example showing that `__annotations__` is not
available on pickled compiled functions. This does work correctly for top-level
functions, but not for nested ones.
```shell
pytest tests/test_annotations.py
```

### cloudpickle

This folder contains code from all the other examples, but uses cloudpickle
instead of dill to pickle the compiled functions, and does not make use of the
Nuitka dill plugin. Most examples actually work fine here, except for the
nested defaults which complains about an unknown opcode.
```shell
pytest tests/test_cloudpickle.py
```

### defaults

This folder contains an example of accessing the `__defaults__` of a function
defined inside another function. This test throws a segfault.
```shell
pytest tests/test_defaults.py
```

### namespace_package

This folder follows a structure similar to our internal Python libraries.
Although the package build and compilation runs without error, an exception is
thrown at import time. This can be reproduced by running
```shell
pytest tests/test_namespace_package.py
```
