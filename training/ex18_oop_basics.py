class Employee:
    # variables declared and initialized here are not part of the objects, but part of the class
    # like `static` in Java/C#
    DEPARTMENTS = ['ADMIN', 'ACCOUNTING', 'MARKETING', 'PRODUCTION']


if __name__ == '__main__':
    # Employee emp1; // In C++ this is an object while in Java/C# this is a reference (emp1 = new Employee())
    emp1 = Employee()
    print(f'id of emp1 is {id(emp1)}')
    print(f'emp1 is {emp1}')
    emp2 = Employee()
    print(f'id of emp2 is {id(emp2)}')
    print(f'emp2 is {emp2}')

    print(f'emp1.departments = {emp1.DEPARTMENTS} and its id = {id(emp1.DEPARTMENTS)} ')
    print(f'emp2.departments = {emp2.DEPARTMENTS} and its id = {id(emp2.DEPARTMENTS)}')

    # making changes to `DEPARTMENTS` IN Employee class using any object will affect all other objects
    emp1.DEPARTMENTS.append('SALES')  # developers are not supposed to do this
    print(f'emp1.departments = {emp1.DEPARTMENTS} and its id = {id(emp1.DEPARTMENTS)} ')
    print(f'emp2.departments = {emp2.DEPARTMENTS} and its id = {id(emp2.DEPARTMENTS)}')

