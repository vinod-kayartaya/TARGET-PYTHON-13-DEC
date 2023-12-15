def dir2(obj):
    return [attribute for attribute in dir(obj) if not attribute.startswith('_')]


def reverse(s: str) -> str:
    if type(s) is not str:
        raise TypeError('Input must be a str')
    return s[::-1]

# open a python REPL from your work folder
# and import this dir2 function like this:
# from my_utils import dir2
# and then check the non-dunder attributes of few types (str, int, list, tuple, ..)
# dir2(list)

# Immutables:
# scalars --> int, float, str, bool
# containers --> tuple

# Mutables/ updatables:
# containers --> list, dict, set
