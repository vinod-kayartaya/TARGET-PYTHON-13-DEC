class Employee:
    DEPARTMENTS = ['ADMIN', 'ACCOUNTING', 'MARKETING', 'PRODUCTION']

    def __init__(self, **kwargs):

        _dept = kwargs.get('department', Employee.DEPARTMENTS[0])
        if _dept is not None and _dept not in Employee.DEPARTMENTS:
            raise ValueError(f'Invalid department. Must be one of {Employee.DEPARTMENTS}')

        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary', 35000)
        self.department = kwargs.get('department', Employee.DEPARTMENTS[0])

    def __str__(self):
        _name = None if self.name is None else f'"{self.name}"'
        _dept = None if self.department is None else f'"{self.department}"'
        return f'Employee(id={self.id}, name={_name}, salary={self.salary}, department={_dept})'

    def __setattr__(self, key, value):
        # print(f'__setattr__ is called with key={key} and value={value}')
        if key not in ('id', 'name', 'salary', 'department'):
            raise AttributeError(f'Invalid attribute - {key}')
        super().__setattr__(key, value)  # call to the __setattr__ in the 
        # `object` class (which is the parent/super/base class)
        # which is actually assigning the `value` to the respective member variable


if __name__ == '__main__':
    emp1 = Employee(id=1122, department='ACCOUNTING')
    # print(dir(emp1))
    emp2 = Employee(id=1221, name='Ramesh', salary=44000, department=None)

    emp1.name = 'Vishal'  # __setattr__() is called here
    emp1.salary = 123000
    emp1.department = 1234
    # emp1.email = 'vishal@xmpl.com'  # uncomment to see the error at the runtime

    print(emp1)  # emp1.__str__() is called automatically
    print(emp2)
