import functools
import traceback

import debugpy


def debug(error, port=5678):
    print(f"Waiting for debugger to attach on {port}\n")
    debugpy.listen(5678)
    debugpy.wait_for_client()
    traceback.print_exc()
    raise error


def debug_on_exception(*exceptions):
    if not exceptions:
        exceptions = (AssertionError,)

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except exceptions as error:
                debug(error)

        return wrapper

    return decorator
