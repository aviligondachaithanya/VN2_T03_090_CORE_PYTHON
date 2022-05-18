## Problem:1

# class Person:
#     def __init__(self, name, age, occupation, address):
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#         self.address = address
#
#     def get_Per_details(self):
#         print("Person_Details:", self.name, self.age, self.occupation, self.address)
#
# chaithanya = Person('chaithanya_aviligonda', 24, 'engineer', 'Anantapur')
# chaithanya.get_Per_details()

# ## Problem:2
# class Mobile:
#     def __init__(self, brand, colour, model, price):
#         self.brand = brand
#         self.colour = colour
#         self.model = model
#         self.price = price
#
# # variablename = classname()
# m1 = Mobile('oppo', 'black', 3.4, 100000)
# m2 = Mobile('vivo', 'black,white', 4.2, 80000)
# print(m1)
# print(m1.brand, m1.colour, m1.model, m1.price)
# print(m2)
# print(m2.brand, m2.colour, m2.model, m2.price)


## Probelm:3
# class Laptop:
#     def __init__(self, brand, colour, configuration, price, model):
#         self.brand = "lenovo"
#         self.colour = " white"
#         self.configuration = "I7"
#         self.price = 65000
#         self.model = "touch"
#
#     def get_laptop_info(self):
#         print("Laptop details  are:", self.brand, self.model)
#
# x1 = Laptop('lenovo', 'white', 'I7', 65000, 'touch')
# x1.get_laptop_info()

## Problem:4 Salary Hikeing
# class Employee:
#     def __init__(self, name, age, id, designation, salary, mobile_no ):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.designation =designation
#         self.salary = salary
#         self.mobile_no = mobile_no
#
#     def get_Employee_info(self):
#         self.salary = self.salary+self.salary*20/100
#         print("Employee Details:", self.name, self.age, self.id, self.designation, self.salary, self.mobile_no)
#
# E1 = Employee('CHAITHANYA', 25, 999, 'engineer', 40000, 9440720867)
# E1.get_Employee_info()
#
# E2 = Employee('Mahesh', 25, 100, 'engineer', 38000, 9490342867)
# E2.get_Employee_info()
#
# E3 = Employee('Vannur', 25, 101, 'engineer', 36000, 7207066811)
# E3.get_Employee_info()

##Problem:5

# class Student:
#     def __init__(self, name, id, father_details, occupation, address, contact ):
#         self.name = name
#         self.id = id
#         self.father_details = father_details
#         self.occupation =occupation
#         self.address = address
#         self.contact = contact
#
#     def get_student_info(self):
#         print("student details:", self.name, self.id, self.father_details, self.occupation, self.address, self.contact)
#
# S1 = Student('chaithanya', 2355, 'chalapathi', 'business', 'anantapur', 9440720867 )
# S1.get_student_info()


# ## Problem:6
# class Student:
#     def __init__(self, name, id, marks, year, address, contact ):
#         self.name = name
#         self.id = id
#         self.marks = marks
#         self.year = year
#         self.address = address
#         self.contact = contact
#
#     def get_student_info(self):
#         print("student details:", self.name, self.id, self.marks, self.year, self.address, self.contact)
# #
# s1_name = input("Enter student name:")
# s1_id = int(input("Enter id:"))
# s1_marks = float(input("Enter marks:"))
# s1_year = int(input("Year:"))
# s1_address = input("Address:")
# s1_contact = int(input("Enter contact number:"))
#
# chaithanya = Student(s1_name, s1_id, s1_marks, s1_year, s1_contact, s1_address)
# chaithanya.get_student_info()

# chaithanya = Student('chaithanya', 99, 99.99, 2022, 'atp', 9440720867)
# chaithanya.get_student_info()
#
# smiley = Student('smiley', 11, 11, 2022, 'atp', 9849410775)
# smiley.get_student_info()
#
# print(chaithanya, id(chaithanya), type(chaithanya) )
# print(chaithanya)
# print(smiley)

## Problem:7
class ITDept:
    def __init__(self, name, domain, experience, company_name):
        self.name = name
        self.domain = domain
        self.experience = experience
        self.company_name = company_name

    def get_ITDept_info(self):
        print("IT Employees Details:", self.name, self.domain, self.experience, self.company_name )

IT1 = ITDept ('chaithanya', 'python_developer', 4, 'vn2_solutions')
IT1.get_ITDept_info()