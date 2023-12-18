"""
A function can receive different types of parameters:

1. positional parameters
2. *args --> variable length arguments
3. **kwargs --> key/value pairs of variable length arguments
"""


# def print_emp_info(id, name, email, salary, dept):
# def print_emp_info(*args):
#     emp_id, name, email, salary, dept = args
def print_emp_info(**kwargs):
    if 'emp_id' not in kwargs:
        raise KeyError('emp_id is required, but missing')
    if 'name' not in kwargs:
        raise KeyError('name is required, but missing')

    print(f"""Employee details:
    ID        : {kwargs.get('emp_id')}
    Name      : {kwargs.get('name')}
    Email     : {kwargs.get('email')}
    Salary    : {kwargs.get('salary', 25000)}
    Department: {kwargs.get('dept', 'ACCOUNTING')}
    """)
    # print(f'kwargs type is --> {type(kwargs)}')
    # print(f'kwargs is {kwargs}')


if __name__ == '__main__':
    print_emp_info(name='Ramesh', emp_id=452, salary=55000, dept='ADMIN')
    emp = dict(name='Rohit', email='rohit@xmpl.com', emp_id=2233)
    print_emp_info(**emp)
