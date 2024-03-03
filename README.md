# Afterthought

Afterthought allows you to always have an attachable debugger ready to use, even when you don't want to use it, and without changing how you run your code.

By default it is setup and tested with vscode, feel free to contribute to add support for other debuggers.

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
