
#
# def product(x, y):
#     p = x + y
#     print(p)

# def product(x, y, z):
#     p = x + y + z
#     print(p)
# #
# def product(w, x, y, z):
#     p = w + x + y+ z
#     print(p)


# product(1, 2)
# product(1, 2, 3)
# product(1, 2, 3, 4 )

#from multipledispatch import dispatch

# @dispatch(int, int)
# def product(a , b):
#     p = a + b
#     print(p)
#
# @dispatch(float, float, float)
# def product(a, b, c):
#     p = a + b + c
#     print(p)
# product(1.1, 2.3, 3.3)
#
# @dispatch(str, str, str)
# def product(a, b, c):
#     p = a + b + c
#     print(p)
#
# product ('welcome ', 'vn2 ', 'IT Solutions')

# class Employee:
#     def __init__(self, name, salary, project):
#         self.name = name
#         self.salary = salary
#         self.project = project
#
#     def show(self):
#         print("Employee details:", self.name,  self.salary)
#
#     def work(self):
#         print("working details:", self.name, 'is working on', self.project)
#
# emp = Employee('chaithanya', 62000, 'VN2')
# emp.show()
# emp.work()

# class Super:
#     def __init__(self, var1, var2, var3):
#         self.var1 = var1
#         self._var2 = var2
#         self.__var3 = var3
#
#     def displaypublicmembers(self):
#         print("public members:", self.var1)
#
#     def displayprotectedmembers(self):
#         print("protect members:", self._var2)
#
#     def displayprivatemembers(self):
#         print("private members:", self.__var3)
#
# class sub(super):
#
#     def __init__(self, var1, var2, var3):
#               super.__init__(self, var1, var2, var3)
#
#     def accessprotectedmembers(self):
#         self.accessprotectedmembers()
#
# obj = ('welcome', 'to', 'VN2')
# obj.displaypublicmembers()
# obj.displayprotectedmembers()
# obj.displayprivatemembers()


class A:
    x = 10
    def m1(self):
        print('one')

class B(A):
    y = 20
    def m2(self):
        print('two')
print(B.x)
print(B.y)
b = B()
# B.m1()
# B.m2()

class A:
    a = 10
    def m1(self):
        print('one')

class B(A):
    b =20
    def m2(self):
        print('two')

class C(B):
    c = 30
    def m3(self):
        print('three')

class D(C):
    d = 40
    def m4(self):
        print('four')

print(C.c)
print(D.d)
print(A.a)
print(B.b)






















































































































































































































































