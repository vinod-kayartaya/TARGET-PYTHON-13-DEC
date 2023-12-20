class A:
    def f1(self):
        print('A.f1() called')


class B(A):
    def f2(self):
        print('B.f2() called')

    def f4(self) -> None:
        print('B.f4() called')


class C(A):
    def f3(self):
        print('C.f3() called')

    def f4(self, x, y) -> int:
        print(f'C.f4() called with {x} and {y}')
        return x+y


class D(B, C):
    pass


if __name__ == '__main__':
    d1 = D()
    d1.f1()
    d1.f2()
    d1.f3()
    d1.f4()  # B.f4() called
    C.f4(d1, 10, 20)  # you are calling f4 from C using the d1 as the invoking object
    print(D.mro())
