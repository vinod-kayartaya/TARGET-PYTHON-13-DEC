class Employee:
    def __init__(self, emp_id=None, name=None, salary=25000):
        # `self` is the reference to the newly constructed object
        # in C++/Java/C# `self` is equivalent of `this` keyword
        # although `self` is the name preferred, we can give any other name to that variable
        print(f'Employee.__init__() called and id of self is {id(self)}')
        # since `self` is a reference to the newly constructed object (which can grow/shrink), we can
        # add more variables in that place
        self.id = emp_id
        self.name = name
        self.salary = salary

    def print(self):
        print('Employee details: ')
        print(f'ID       : {self.id}')
        print(f'Name     : {self.name}')
        print(f'Salary   : {self.salary}')
        print()


if __name__ == '__main__':
    emp1 = Employee(1123, 'Vishal')  # at this time, python executes the __init__() method for the newly constructed object
    print(f'id of emp1 is {id(emp1)}')
    emp1.print()  # here, emp1 is passed implicitly by python as the first argument to the print() function
    
    emp2 = Employee(1212, 'Vijay', 34000)
    print(f'id of emp2 is {id(emp2)}')
    emp2.print()
