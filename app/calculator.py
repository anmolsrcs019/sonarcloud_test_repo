from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b