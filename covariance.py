from typing import TypeVar, Callable

T = TypeVar("T", covariant=True)


## Кортежи в Python ковариантны
def first_item(t: tuple[object, ...]) -> T:
    return t[0]


names: tuple[str, ...] = ("Alice", "Bob")
result: str = first_item(names)  # Работает нормально. str является наследником object


# Кортежи (tuple) ковариантны, так как они неизменяемы и из них можно только читать данные:
tuple_of_strings: tuple[str, ...] = ("a", "b")
tuple_of_objects: tuple[object, ...] = tuple_of_strings  # Это безопасно

# ------------------

## Функции также ковариантны по возвращаемому значению
def get_string() -> str:
    return "Hello"

# Функция, возвращающая str, может использоваться там, где ожидается функция, возвращающая object
def expect_func_returning_object(f: Callable[[], object]) -> None:
    obj = f()
    print(type(obj))


expect_func_returning_object(get_string)
# Это безопасно, так как str является подтипом object
