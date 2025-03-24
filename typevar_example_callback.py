from typing import Callable, TypeVar

T = TypeVar('T')


def process_data(data: T, callback: Callable[[T], T]) -> T:
    return callback(data)


def double_value(value: int) -> int:
    return value * 2

def hello(name: str) -> str:
    return f'Hello, {name}'

input_data = 5
result = process_data(input_data, double_value)
print(result)  # Вывод: 10

input_data = 'Anton'
result = process_data(input_data, hello)
print(result)

