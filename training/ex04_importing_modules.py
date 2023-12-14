import ex03_if_elif_else


# the value of __name__ is either '__main__' (when the module is being run)
# or the base name of the file (when the module is imported)
if __name__ == '__main__':
    si = ex03_if_elif_else.calculate_simple_interest(1000000, 36)
    print(f'si is {si}')
