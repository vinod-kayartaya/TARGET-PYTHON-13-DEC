"""
List comprehension can be used to get a new list from the original list
1. to filter the content of the original list
2. to convert the elements of the original elements into some other elements (map)
"""
import math


def is_prime(num: int) -> int:
    if num <= 1:
        return False

    limit = num // 2
    for d in range(2, limit+1):
        if num % d == 0:
            return False

    return True


def main():
    nums = [200, 10, 99, 22, 10, 40, 59, 29, 93, 212]
    even_nums = [each_num for each_num in nums if each_num % 2 == 0]
    odd_nums = [n for n in nums if n % 2]  # 0 --> False, non-zero --> True
    print(nums)
    print(even_nums)
    print(odd_nums)
    halves = [n/2 for n in nums]
    squares = [n*n for n in nums]
    square_roots = [math.sqrt(n) for n in nums]
    print(f'squares is {squares}')
    print(f'halves is {halves}')
    print(f'square_roots is {square_roots}')
    primes = [n for n in range(1, 501) if is_prime(n)]
    print(f'primes is {primes}')


if __name__ == '__main__':
    main()
