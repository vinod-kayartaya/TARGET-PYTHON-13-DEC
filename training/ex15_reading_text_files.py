"""
When the `open` function is called, it returns an object representing a stream with the following attributes:
['buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'reconfigure',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'write_through',
 'writelines']
"""
FILENAME = '/Users/vinod/Desktop/TARGET-PYTHON-13-DEC/training/names.txt'


def file_read_method1():
    file = open(FILENAME, mode='r')
    print(f'file.closed is {file.closed}')
    print(f'file.readable() is {file.readable()}')
    print(f'file.writable() is {file.writable()}')
    content = file.read()
    file.close()  # releases the memory allocated by the native C++ code; not calling this may result in resource leak
    print(f'file.closed is {file.closed}')

    print(content)


def file_read_method2():
    file = None
    try:
        file = open(FILENAME, mode='r', encoding='utf-8')
        list_of_lines = file.readlines()

        for each_line in list_of_lines:
            print(each_line, end='')
        # try with `return` or `exit(0)` or `raise ValueError('....')`
    except FileNotFoundError as err:
        print(f'Whoops! There was an error - {err}')
    except UnicodeDecodeError as err:
        print(f'Something went wrong while reading - {err}')
    finally:
        print('executing the `finally` block')
        if file is not None:
            print('we are now closing the file')
            file.close()
    print('end of file_read_method2()')


def file_read_method3():
    try:
        # use the context manager block while working with resources (like file, db connection, socket etc)
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            # just when the context manager block ends, `file.close()` is automatically called
            while True:
                a_line = file.readline()
                if a_line == '':
                    break
                print(a_line, end='')
    except FileNotFoundError as err:
        print(f'Whoops! There was an error - {err}')
    except UnicodeDecodeError as err:
        print(f'Something went wrong while reading - {err}')


def file_read_method4():
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            for a_line in file:  # remember `file` is a stream, and looping over that will give you one line at a time
                print(a_line, end='')
    except FileNotFoundError as err:
        print(f'Whoops! There was an error - {err}')
    except UnicodeDecodeError as err:
        print(f'Something went wrong while reading - {err}')


def main():
    file_read_method4()
    print('end of script.')


if __name__ == '__main__':
    main()
