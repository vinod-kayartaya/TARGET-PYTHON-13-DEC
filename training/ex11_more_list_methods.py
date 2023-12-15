"""
List methods:
'append', 'insert', 'clear', 'copy', 'count', 'extend', 'index', 'pop', 'remove', 'reverse', 'sort'
"""


def main():
    nums = [200, 10, 99, 22, 10, 2, 3, 40, 59, 29, 93, 10]
    c = nums.count(10)
    print(f'10 repeats {c} times in nums')
    c = nums.count(100)
    print(f'100 repeats {c} times in nums')
    nums.extend([11, 22, 33])
    print(f'nums = {nums}')
    nums += [44, 55]
    print(f'nums = {nums}')
    names = ['vinod', 'shyam', 'kumar']
    print(f'names = {names}')
    names += 'sundar'  # a str is considered as a list of characters. i.e, 'sundar' --> ['s', 'u', 'n', 'd', 'a', 'r']
    print(f'names = {names}')
    n = 40
    if n in nums:
        i = nums.index(n)
        print(f'{n} is found at index {i} of nums')
    else:
        print(f'{n} is not found in nums')

    for _ in range(3):
        p = nums.pop()
        print(f'after popping {p} from nums, it is {nums}')

    i = 6
    if i < len(nums):
        p = nums.pop(i)  # pop element at 4; if 4 is invalid index, IndexError will be raised
        print(f'after popping {p} at index {i} from nums, it is {nums}')
    else:
        print(f'{i} is an invalid index')





    n = 106
    if n in nums:
        nums.remove(n)
        print(f'{n} is removed from nums, and it is now {nums}')
    else:
        print(f'{n} is not in nums')

    nums.reverse()
    print(f'after reversing, the nums is {nums}')
    nums.sort()
    print(f'after sorting, the nums is {nums}')
    nums.sort(reverse=True)
    print(f'after reverse sorting, the nums is {nums}')


if __name__ == '__main__':
    main()
