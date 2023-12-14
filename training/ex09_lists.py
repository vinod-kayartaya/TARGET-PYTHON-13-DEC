"""
- `list` is an ordered collection of values (can be anything - scalars, containers, user-defined objects, functions...)
- Each element is accessed using an index, and the index starts with 0
- The size of the list can be obtained using the built-in function called `len`
- If index is outside the range, then `IndexError` will be raised
- following are the attributes of a list object:
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
import math


def main_method():
    list1 = ['vinod', 50, False, (10, 20, 30), 2.5]
    print(f'element at index 3 is {list1[3]}')
    list1.append(math.pi)
    print(list1)
    list1.insert(1, 'bangalore')
    print(list1)
    list1.insert(0, 1234)
    print(list1)
    list1.insert(-100, 999)
    # if -100 is an index beyond the first index (i.e, -9) then it will simply insert at index 0
    print(list1)
    list1.insert(100, 222)
    # if -100 is an index beyond the last index (i.e, 9) then it will simply insert at the end
    print(list1)

    print(f'last element in the list1 is {list1[-1]}')
    print(f'the first element is {list1[-10]}')


if __name__ == '__main__':
    main_method()
