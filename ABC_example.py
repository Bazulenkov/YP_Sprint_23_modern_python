from abc import ABC, abstractmethod


#  class Animal(metaclass=ABCMeta):
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """make sound"""

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Running on four legs"


dog = Dog()
