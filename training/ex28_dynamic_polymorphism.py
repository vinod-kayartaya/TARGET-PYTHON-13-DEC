from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        print('Animal is generic; I don\'t know how it speaks.')

    def written_by(self) -> str:
        return 'Vinod'


class Dog(Animal):  # Dog IS-A Animal
    def speak(self):
        print('Bow bow')


class Tiger(Animal):  # Tiger IS-A Animal
    def speak(self):
        print('Grr...')


class Cat(Animal):  # Cat IS-A Animal
    def speak(self):
        print('Meow...')


class Human(Animal):
    def speak(self):
        print('Hello, there!')

    def written_by(self) -> str:
        return 'VKK'


# polymorphic method
def speak_with_animal(a1: Animal) -> None:
    if not isinstance(a1, Animal):
        raise TypeError('must pass Animal object')

    print(f'Now talking to a {str(type(a1))[17:][:-2]} written by {a1.written_by()}')
    a1.speak()  # different output based on what object it refers to


if __name__ == '__main__':
    d1 = Dog()  # is-a Animal
    t1 = Tiger()  # is-a Animal
    c1 = Cat()  # is-a Animal
    h1 = Human()

    speak_with_animal(d1)
    speak_with_animal(t1)
    speak_with_animal(c1)
    speak_with_animal(h1)
    # speak_with_animal(123)

