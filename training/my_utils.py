def to_dict(line1: str, line2: str, delim=',') -> dict:
    keys = [k.strip() for k in line1.strip().split(delim)]
    keys = [int(k) if k.isdigit() else k for k in keys]
    values = [v.strip() for v in line2.strip().split(delim)]
    values = [int(v) if v.isdigit() else v for v in values]
    return dict(zip(keys, values))


def csv2json(csv_filename: str) -> str:
    # assumption --> filename is just the filename without the path
    import time
    import json
    json_filename = f'{csv_filename[:-4]}_{time.time()}.json'
    try:
        with open(csv_filename) as csv_file:
            header = csv_file.readline()
            data = [to_dict(header, a_line) for a_line in csv_file]
            with open(json_filename, mode='w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)
                return json_filename
    except OSError as err:
        print(err)


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
