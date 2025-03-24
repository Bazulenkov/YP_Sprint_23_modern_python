from typing import Protocol, runtime_checkable


@runtime_checkable
class Drinkable(Protocol):
    def drink(self):
        print("simple drink")


def bar(obj: Drinkable):
    obj.drink()


class Bottle:
    @staticmethod
    def drink():
        print("bottle drink")


bottle = Bottle()
print(isinstance(bottle, Drinkable))

bar(bottle)

# А теперь передадим в кач-ве параметра число. Это тоже объект, но у него нет метода
# drink.
# bar(15)
# получим ошибку в mypy.



# Дока
# https://peps.python.org/pep-0544/#defining-a-protocol
# https://docs.python.org/3/library/typing.html#typing.Protocol