# Afterthought

[![PyPI version](https://badge.fury.io/py/afterthought.svg)](https://badge.fury.io/py/afterthought)

A [debugpy](https://github.com/microsoft/debugpy) alternative to [pdb.post_mortem()](https://docs.python.org/3/library/pdb.html#pdb.post_mortem) that allows you to attach any debugger to your code after an exception has been raised.

**By default it is setup and tested with vscode, but feel free to contribute to add support for other debuggers.**

## Installation

```bash
pip install afterthought
```

## Usage

```python
import afterthought


def bombs():
    a = []
    print(a[0])


if __name__ == "__main__":
    try:
        bombs()
    except Exception as e:
        afterthought.debug(e)

```

You can then connect using any tool that supports https://github.com/microsoft/debugpy


## Function Decorators

You can also use the `@afterthought.debug_on_exception` decorator to automatically attach the debugger to any function that raises an exception.

```python
import afterthought


@afterthought.debug_on_exception(IndexError)
def bombs():
    a = []
    print(a[0])


if __name__ == "__main__":
    bombs()
```

## VSCode Configuration

Add the following configuration to your `.vscode/launch.json` file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Remote Attach",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ]
        }
    ]
}
```
