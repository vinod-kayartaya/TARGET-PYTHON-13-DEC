"""
slice operations on a list give us a sublist
a_list[index]
a_list[from_index: to_index] where to_index == from_index + item_count
from_index is inclusive, but to_index is exclusive

both from_index and to_index are optional
1. if to_index is omitted, all elements from the from_index till the end will be given
2. if from_index omitted, then from_index is considered to be 0

a_list[from_index: to_index: step]
"""
from my_utils import reverse


def main():
    nums = [200, 10, 99, 22, 10, 40, 59, 29, 93, 212]
    print(f'nums = {nums}')
    print(f'len of nums is {len(nums)}')
    print(f'last element in nums is {nums[-1]}')
    sub_nums = nums[2:6]
    print(f'4 elements from index 2 in nums is {sub_nums}')
    sub_nums = nums[4:]  # same as nums[4:len(nums)]
    print(f'elements from index 4 till the end are {sub_nums}')
    sub_nums = nums[:5]
    print(f'elements till index 5 (excluding) are {sub_nums}')
    # nums_at_even_indices = nums[0: len(nums): 2]
    nums_at_even_indices = nums[::2]
    print(f'nums_at_even_indices = {nums_at_even_indices}')
    nums_at_odd_indices = nums[1::2]
    print(f'nums_at_odd_indices = {nums_at_odd_indices}')
    reverse_nums = nums[::-1]
    print(f'reverse_nums = {reverse_nums}')
    my_name = 'vinod'
    # my_name_in_rev = my_name[::-1]
    my_name_in_rev = reverse(my_name)
    print(f'my name is {my_name} and my name in reverse is {my_name_in_rev}')


if __name__ == '__main__':
    main()
