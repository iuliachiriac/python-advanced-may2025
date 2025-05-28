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
