"""
`range` is a class, an object of which represents a sequence of numbers
"""


def multiplication_table(num: int, limit=10) -> None:
    for index in range(1, limit+1):
        print(f'{num} X {index} = {num*index}')


def factorial(num: int) -> int:
    if num < 1:
        raise ValueError('Factorial of 0 or negative numbers are not defined')

    f = 1
    for n in range(num, 1, -1):
        f *= n

    return f


def main():
    n = int(input('Enter a number: '))
    # multiplication_table(n)
    f = factorial(n)
    print(f'the factorial of {n} is {f}.')


if __name__ == '__main__':
    main()
