class Employee:
    DEPARTMENTS = ['ADMIN', 'ACCOUNTING', 'MARKETING', 'PRODUCTION']

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')  # call the setter, instead of assigning directly to the private variable
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary', 35000)
        self.department = kwargs.get('department', Employee.DEPARTMENTS[0])

    # a getter/accessor/readable property called 'id'
    @property
    def id(self):
        # print('(getter for id is called)')
        return self.__id

    # a setter/mutator/writable property called 'id'. For a setter to exist, getter is mandatory
    @id.setter
    def id(self, value):
        # validate before assignment
        if value is not None and type(value) is not int:
            raise TypeError('Invalid type for id. Must be an int.')
        if value is not None and (value <=0 or value >= 99999):
            raise ValueError('Invalid value for id. Must be between 1 and 99999')
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('name must be a str')
        if value is not None and (len(value) <3 or len(value) > 15):
            raise ValueError('name must be between 3 to 15 letters')

        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('salary must be a number')
        if value is not None and (value < 35000 or value > 250000):
            raise ValueError('salary must be between Rs.35000/- and Rs.250000/-')
        self.__salary = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if value is not None and type(value) is not str:
            raise TypeError('department must be a str')
        if value is not None:
            value = value.upper()
        if value is not None and value not in Employee.DEPARTMENTS:
            raise ValueError(f'department must be one of {Employee.DEPARTMENTS}')

        self.__department = value

    def __str__(self):
        _name = None if self.name is None else f'"{self.__name}"'
        _dept = None if self.department is None else f'"{self.department}"'
        return f'Employee(id={self.id}, name={_name}, salary={self.salary}, department={_dept})'

    def print(self):
        print('Employee details: ')
        print(f'ID         : {self.id}')
        print(f'Name       : {self.name}')
        print(f'Salary     : {self.salary}')
        print(f'Department : {self.department}')
        print()


if __name__ == '__main__':
    emp1 = Employee(id=1212, name='Vishal')
    emp2 = Employee(id=1234, name='Ramesh', salary=55000, department='MARKETING')

    # print(dir(emp1))
    emp1.__salary = -45000  # doesn't have any effect on the internal member variable __salary
    emp1.__department = 1234  # I want this to result into an error
    # print(dir(emp1))

    print(emp1)
    print(emp2)

    emp1.print()
    emp2.print()

    emp1.id = 1122  # this is where the setter is called with self=emp1 and value=3456
    emp1.name = 'Raj'
    emp1.salary = 120000
    emp1.department = 'production'

    emp1.print()
    print(f'emp1.id is {emp1.id}')  # the `def id(self)` is called here

