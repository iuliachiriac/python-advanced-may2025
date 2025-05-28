from functools import wraps


def make_pretty(func):
    @wraps(func)  # inner = wraps(func)(inner)
    def inner(*args, **kwargs):
        print(f"I got decorated. I am {func} and was called with "
              f"args={args} and kwargs={kwargs}.")
        return func(*args, **kwargs)
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    """Prints a greeting message for name"""
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=0):
    return nr - step


# ordinary = make_pretty(ordinary)  # make_pretty.<locals>.inner
# print("ordinary =", ordinary)

ordinary()  # make_pretty.<locals>.inner()
greet("Anna")  # make_pretty.<locals>.inner("Anna")
greet(name="Jane")

result = decrement(10, step=2)  # make_pretty.<locals>.inner(10, step=2)
print(f"Decrement result: {result}")

help(greet)
print(greet.__name__, greet.__doc__)
