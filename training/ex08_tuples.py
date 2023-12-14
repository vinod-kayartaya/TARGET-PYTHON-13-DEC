"""
`tuple` is a class, an object of which is a collection/container of values.
The collection itself is immutable, meaning, once the tuple is created, it cannot be modified:
1. cannot add new elements
2. cannot delete existing elements

If the element itself is a mutable value (such as list/dict/set or an object of a user defined class), the element
itself can be modified, but the tuple remains intact
"""
from my_utils import dir2


def avg(*nums):
    # print(f'type of nums is {type(nums)}')
    return sum(nums)/len(nums)


def sub_total(*nums):
    return sum(nums), len(nums), sum(nums) / len(nums)


def main():
    t1 = (10, 20, '30', 1.0, [12, 22], 30, 10, 303)
    print(f'the attributes of t1 are: {dir2(t1)}')
    print(f'element at index 0 is {t1[0]}')
    print(f'element at index 1 is {t1[1]}')
    print(f'element at index 2 is {t1[2]}')
    # t1[1] = 22  # TypeError: 'tuple' object does not support item assignment
    t1[4].append(100)
    # print(f'element at index 3 is {t1[3]}')  # IndexError is raised by the subscript operator [3]
    n = 10
    if n in t1:
        i = t1.index(n)
        c = t1.count(n)
        print(f'{n} is at index {i} and found {c} times in the tuple')
    else:
        print(f'{n} is not in the tuple t1')

    print(f'there are {len(t1)} elements in t1')
    for each_element in t1:
        print(f'{each_element} --> {type(each_element)}')

    average = avg(10, 20, 10, 20, 40, 10, 203, 482, 38)
    print(f'average = {average}')
    t2 = (1, 2, 3, 4, 5, 6)
    average = avg(*t2)  # spread the members of t2 instead of sending t2 as the only argument
    print(f'average = {average}')

    a, b, c = 10, 20, 30
    print(f'type of a is {type(a)}')
    print(f'a={a}, b={b}, c={c}')

    st = sub_total(10, 20, 30, 40)
    print(f'st = {st}')
    total, count, avrg = sub_total(10, 20, 30, 40)
    print(f'total={total}, count={count}, avrg={avrg}')


if __name__ == '__main__':
    main()
