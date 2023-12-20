class Test:
    def __init__(self, name = None):
        self.name = name

    def print(self):
        """
        This is an example of a non-static method.
        Has access to other members of this object via `self`
        """
        print(f'name = {self.name}')

    @staticmethod
    def print_author_info():
        print('Created by Vinod Kumar')
        print('Phone: 9731424784')
        print('Email: vinod@vinod.co')
        print()

    @classmethod
    def say_hello(cls, name, city):
        c1 = cls()  # same as Test()
        print(cls)
        print(c1)
        print(f'Hello {name}. When did you come from {city}?')


if __name__ == '__main__':
    t1 = Test('Vinod')
    t1.print()  # t1 is the first argument to print() function (i.e, `self`)

    Test.print_author_info()
    t1.print_author_info()  # t1 is not passed as the first argument to print_author_info()

    Test.say_hello('Sanjay', 'Mumbai')
    t1.say_hello('Sanjay', 'Mumbai')
