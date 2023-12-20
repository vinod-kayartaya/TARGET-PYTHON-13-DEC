class Greet:

    def say_hello(self, name):
        print(f'Hello, {name}!')

    def say_hello(self):  # this method replaces the above method
        print('Hello, world!')


if __name__ == '__main__':
    g1 = Greet()
    g1.say_hello()
    g1.say_hello('Vinod')  # problem
