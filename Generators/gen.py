# Simple generator function


def some_gen():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x


# Fibonacci numbers using generator
def fib(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x
