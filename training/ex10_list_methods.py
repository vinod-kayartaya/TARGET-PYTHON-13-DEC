"""
List methods:
'append', 'insert', 'clear', 'copy', 'count', 'extend', 'index', 'pop', 'remove', 'reverse', 'sort'
"""
import json


def main():
    nums = [200, 100, 1, 2, 3, 40, 59, 29, 93]
    print(f'nums is {nums}, id(nums) is {id(nums)}')
    nums.clear()  # empties the list content
    print(f'nums is {nums}, id(nums) is {id(nums)}')
    items = [200, 100, 1, 2, 3, [40, 59, 29], 93]
    print(f'item count in items is {len(items)}')
    # enumerate(items) --> [(0, 200), (1, 100), (2, 1), (3, 2), (4, 3), (5, [40, 59, 29]), (6, 93)]
    for index, each_item in enumerate(items):
        print(f'index = {index}, each_item = {each_item}')

    new_items = items.copy()
    print(f'items is {items}')
    print(f'new_items is {new_items}')
    new_items[0] = 75
    print(f'items is {items}')
    print(f'new_items is {new_items}')
    new_items.append(999)
    print(f'items is {items}')
    print(f'new_items is {new_items}')
    new_items[5].append(888)
    print(f'items is {items}')
    print(f'new_items is {new_items}')

    # creating a deep copy of a python object (json serializable) using the json module methods - dumps, loads
    items_str = json.dumps(items)
    another_items = json.loads(items_str)
    another_items[5].append(777)
    print()
    print(f'items = {items}')
    print(f'another_items = {another_items}')

    print(f'id(items[5]) = {id(items[5])}')
    print(f'id(new_items[5]) = {id(new_items[5])}')
    print(f'id(another_items[5]) = {id(another_items[5])}')

    print(f'id(items[5][0]) = {id(items[5][0])}')
    print(f'id(another_items[5][0]) = {id(another_items[5][0])}')
    print(f'id(40) is {id(40)}')


if __name__ == '__main__':
    main()
