class Employee:
    DEPARTMENTS = ['ADMIN', 'ACCOUNTING', 'MARKETING', 'PRODUCTION']

    def __init__(self, **kwargs):
        # call the setter, instead of assigning directly to the private variable
        self.id = kwargs.get('id')
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

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.salary = other if self.salary is None else self.salary + other
        elif type(other) is str:
            self.name = other if self.name is None else self.name + other
        else:
            raise TypeError('this operator works only with numbers and strings')
        return self

    def __add__(self, other):
        if type(other) in (int, float):
            return other if self.salary is None else self.salary + other
        elif type(other) is str:
            return other if self.name is None else self.name + other
        else:
            raise TypeError('this operator works only with numbers and strings')

    def __gt__(self, other):
        if type(other) in (int, float):
            return self.salary > other
        elif isinstance(other, Employee):
            return self.salary > other.salary
        else:
            raise TypeError('this operator works only with numbers and Employees')

if __name__ == '__main__':
    emp1 = Employee(id=1212, name='Vishal')
    emp1 += 500  # 5000 to be added to the salary
    emp1 += ' Kumar'  # ' Kumar' to be concatenated to the name
    emp1.print()
    print(emp1 + ' Malhotra')
    print(emp1 + 4500, end='\n\n')
    emp2 = Employee(id=1234, name='Ramesh', salary=55000, department='MARKETING')
    if emp1 > emp2:  # want to compare the salaries of emp1 and emp2
        print(f'{emp1.name} earns more than {emp2.name}')
    else:
        print(f'{emp1.name} earns less than or equals to {emp2.name}')
    salary_to_compare = 50000
    if emp1 > salary_to_compare:  # want to compare emp1's salary with 50000
        print(f'{emp1.name} earns more than {salary_to_compare}')
    else:
        print(f'{emp1.name} earns less than or equals to {salary_to_compare}')

