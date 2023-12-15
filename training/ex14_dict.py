"""
dict --> dictionary

key/value based collection
"""
from pprint import pprint


def main():
    p1 = dict(fname='Vinod', lname=None, age=50, emails=['vinod@vinod.co', 'vinod@xmpl.com'])
    pprint(p1)
    p1['phones'] = {'9731424784', '9844083934'}
    pprint(p1)
    del p1['age']
    pprint(p1)
    p1['lname'] = 'Kayartaya'
    pprint(p1)
    field = 'fname'
    # print(f'value corresponding to the key {field} is {p1[field]}')
    print(f'value corresponding to the key {field} is {p1.get(field, "Unknown")}')

    print(f'keys in p1 are {p1.keys()}')
    print(f'values in p1 are {p1.values()}')
    print('items in p1 are:')
    for item in p1.items():
        # print(item)
        print(f'{item[0]} --> {item[1]}')

    k = 'fname'
    if k in p1:  # k is checked if it is one of the keys in p1
        v = p1.pop(k)
        print(f'removed the value {v} corresponding to the key {k} from p1')
        print('now the keys/values in p1 are: ')
        pprint(p1)
    else:
        print(f'{k} is not a valid key in p1')

    p2 = dict.fromkeys(['x', 'y', 'z'], 0)
    p2['lname'] = 'Kumar'
    print(f'p2 is {p2}')

    p1.update(p2)
    pprint(p1)


if __name__ == '__main__':
    main()
