from typing import Callable

# Функции контравариантны по аргументам
def print_string(s: str) -> None:
    print(s)


def use_object_consumer(f: Callable[[object], None]) -> None:
    f("Hello")  # str является подтипом object


# Это работает, хотя print_string принимает более конкретный тип (str),
# чем требуемый Callable[[object], None]
use_object_consumer(print_string)
