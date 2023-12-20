from ex22_operator_overloading import Employee
from my_utils import dir2
from pprint import pprint


class SalesPerson(Employee):
    def __init__(self, **kwargs):
        # this makes the inherited __init__ invisible
        self.comm_pct = kwargs.get('comm_pct', 0.0)
        self.target_achieved = kwargs.get('target_achieved', 0.0)
        super().__init__(**kwargs)

    @property
    def comm_pct(self):
        return self.__comm_pct

    @comm_pct.setter
    def comm_pct(self, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('comm_pct must be a number')
        if value is not None and (value < 0 or value > 100):
            raise TypeError('comm_pct must be between 0 to 100')
        self.__comm_pct = value

    @property
    def target_achieved(self):
        return self.__target_achieved

    @target_achieved.setter
    def target_achieved(self, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('target_achieved must be a number')
        if value is not None and value < 0:
            raise TypeError('target_achieved must be >= 0')
        self.__target_achieved = value

    def print(self):
        super().print()
        print(f'Commission%: {self.comm_pct}')
        print(f'Target done: {self.target_achieved}')
        print()


if __name__ == '__main__':
    sp = SalesPerson(id=1234, name='Sujit', department='marketing')
    pprint(dir2(sp))

    sp.comm_pct = 12
    sp.target_achieved = 25000000
    sp += 100000
    sp += ' Nair'

    sp.print()
