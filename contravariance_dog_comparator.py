from typing import TypeVar, Protocol, List  #, Generic

T_contra = TypeVar("T_contra", contravariant=True)


# class Comparator(Protocol, Generic[T_contra]):  # старый синтаксис
class Comparator(Protocol[T_contra]):
    def compare(self, a: T_contra, b: T_contra) -> int: ...


class AnimalComparator:
    @staticmethod
    def compare(a: object, b: object) -> int:
        # Сравнение любых объектов по их ID
        return id(a) - id(b)


class DogComparator:
    @staticmethod
    def compare(a: "Dog", b: "Dog") -> int:
        # Специализированное сравнение для собак по возрасту
        return a.age - b.age



class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Dog({self.name}, {self.age})"


# Функция, использующая компаратор для сортировки собак
def sort_dogs(dogs: List[Dog], comparator: Comparator[Dog]) -> List[Dog]:
    # Создаем копию списка, чтобы не модифицировать оригинал
    result = dogs.copy()

    # Сортировка с использованием переданного компаратора
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if comparator.compare(result[i], result[j]) > 0:
                result[i], result[j] = result[j], result[i]

    return result


# Примеры использования
dogs = [Dog("Барон", 5), Dog("Рекс", 3), Dog("Шарик", 7)]

# Используем общий компаратор для животных
print("Сортировка с AnimalComparator:")
sorted_by_id = sort_dogs(dogs, AnimalComparator())
print(sorted_by_id)

# Используем специализированный компаратор для собак
print("\nСортировка с DogComparator (по возрасту):")
sorted_by_age = sort_dogs(dogs, DogComparator())
print(sorted_by_age)