# class Employee:
#     def __init__(self, eid, name, salary ):
#         print("self address:", self)
#         self.eid = eid
#         self.name = name
#         self.salary = salary
#
#     def get_edata(self):
#         print("Employee Details:", self.eid, self.name, self.salary )
#
# chay = Employee(101, 'chaithnaya aviligonda', 10000)
# chay.get_edata()
#
# raj = Employee(102, 'raja', 50000)
# raj.get_edata()
#

# class Employee:
#     def __init__(self, eid, name, sal):
#         self.eid = eid
#         self.name = name
#         self.sal = sal
#
#     def get_edata(self):
#         print("Employee Details:", self.eid, self.name, self.sal)
#
#     def apply_hike(self, rating):
#         print("apply hike with rating:", rating)
#         if rating>=4 and rating<=5:
#             hike = self.sal*30/100
#             print("Hike is:", hike)
#         elif rating>=3 and rating<=4:
#             hike = self.sal*20/100
#             print("Hike is:", hike)
#         elif rating>=2 and rating<=3:
#             hike = self.sal*10*100
#             print("Hike is:", hike)
#         else:
#             print("Hike is:", 0)

# E1 = Employee(100, 'chaithanya', 12000)
# Employee.get_edata(E1)
# val = int(input("Enter rating:", ))
# Employee.apply_hike(E1, val)
#
# E1.get_edata()
# E1.apply_hike(val)

# E2 = Employee(111, 'smiley', 15000)
# Employee.get_edata(E2)
# val = int(input("Enter rating:"))
# # Employee.apply_hike(E2, val)
#
# class Employee:
#     comp = 'VN2 IT SOLUTIONS'
#     Dept = 'Software'
#     def __init__(self, eid, name, salary):
#         self.eid = eid
#         self.name = name
#         self.salary = salary
#
#     def get_edata(self):
#         print("Employee Details:", self.eid, self.name, self.salary, Employee.comp, Employee.Dept)

# chay = Employee(200, 'chaithanya', 20000)
# chay.get_edata()
#
# raj = Employee(111, 'raja', 10000)
# raj.get_edata()




#
# my_list = ["mani", "madam", "xerox", "pip", "practice", "aa"]
# result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
# print(result)
#
# class Employee:
#     company  = 'VN2_IT SOLUTIONS'
#     emp_coun = 0
#     def __init__(self, eid, name, sal):
#         self.eid = eid
#         self.name = name
#         self.sal = sal
#
#     def get_emp_details(self):
#         print(self.eid, self.name, self.sal, self.company, self.emp_coun)
#
# x = Employee(100, "chaithanya", 20000 )
# x.get_emp_details()
#
#
# # Python program to demonstrate
# # string concatenation
#
# var1 = "Hello"
# var2 = "World"
#
# # , to combine data types with a single whitespace.
# print(var1, var2)

#
# def odd_even(n):
#     if (n%2 == 0):
#         return 'EVEN'
#     elif (n%2 != 0):
#         return 'odd'
#
# n = int(input('Enter any num::' ))
# if (odd_even(n)):
#     print(n, 'num is even')
# else:
#     print(n,'num is odd')
#
#
# def ispalindrome(s):
#     return s == s[::-1]
# s = 'pip'
# ans = ispalindrome()
#
# if ans:
#     print("yes")
# else:
#     print("no")

#
# x= "chaithanya"
# for i in x[::-1]:
#     print(i, end=" ")

# class Employee:
#     comp = 'oracle'
#     e_count = 0
#     def __init__(self, name, contact, eid ):
#         self.name = name
#         self.contact = contact
#         self.eid = eid
#         Employee.e_count += 1
#
#     @classmethod
#     def get_edata(cls):
#         print("Employee details:", cls.comp, cls.e_count)
#
#     def get_empdata(self):
#         print("Employee details:", self.name, self.contact, self.eid)
#
# E1 = Employee('chaithanya', 9440720867, 111)
# E1.get_edata(),E1.get_empdata()
#
# E2 = Employee('raj', 9908656899, 222)
# E2.get_edata(),E2.get_empdata()
#













