from functools import wraps


def log(filename=None):
    def decorators_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def write(message: str) -> None:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write(f"{func.__name__} ok")
                return result
            except Exception as e:
                write(f"{func.__name__} error: {type(e).__name__}: {e}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorators_log
