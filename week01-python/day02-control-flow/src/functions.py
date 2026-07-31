def greet(name: str) -> None:
    """Print a greeting."""
    print(f"Hello {name}")


greet("Emil")


def square(number: int) -> int:
    """Return the square of a number."""
    return number**2


result = square(5)
print(result)


def add(a: int, b: int) -> int:
    return a + b


result = add(3, 4)
print(result)
