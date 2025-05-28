def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(2)
def greet(name):
    print(f"Hello, {name}!")


greet = repeat(2)(greet)

greet("Anna")
print(greet)

def retry(num_times):
    def decorator_repeat(func):
        def exception_handler(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as ex:
                nonlocal num_times
                num_times -= 1
                print(f'Another exception {type(ex).__name__}: {ex}')
                print(f'Remaining tries {num_times}')
                if not num_times:
                    raise ex
        return exception_handler
    return decorator_repeat
