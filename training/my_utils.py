def dir2(obj):
    attributes = []  # or list()
    for each_attribute in dir(obj):
        if not each_attribute.startswith('_'):
            attributes.append(each_attribute)

    return attributes


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
