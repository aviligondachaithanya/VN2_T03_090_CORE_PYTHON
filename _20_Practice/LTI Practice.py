# 37. Write a Python function that accepts a string and calculate the number of upper case letters and lower
# case letters.
#  x = input("Enter name:")
# def count(x):
#     lower = upper = 0
#     for i in x:
#         if(i.islower()):
#             lower = lower+1
#         elif(i.isupper()):
#             upper = upper+1
#     print("upper case:", upper)
#     print("lower case:", lower)
# count(x)


# 36. Write a Python program to reverse a string.
# x = "Chay1234"
# def rev(x):
#     for i in x[::-1]:
#         print(i, end =" ")
# rev(x)

# 35. Write a Python program to convert a list of multiple integers into a single integer.
# L = ['chay', 'chaithanya', 'aviligonda']
# x = str(" ".join(map(str, L)))
# print("Single str: ", x)


# 34. Write a Python program to change the position of every n-th value with the (n+1)th in a list.

# x = [11, 12, 13, 14, 15, 16 ]
# def change(x):
#     for i in x:
#         x.insert(1, 'e')
#         return x
# print(change(x))

# 33. Write a Python program to generate and print a list except for the first 5 elements, where the values are
# square of numbers between 1 and 30 (both included).
# def first():
#     l = list()
#     for i in range(1, 31):
#         l.append(i**2)
#     print(l[5:])
# first()

# 32. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]
# print(color)


# 23. How would you produce a list with unique elements from a list with duplicate elements
# x = ['a','b','c','d','d','d','e','a','b','f','g','g','h']
# list = []
# for i in x:
#     if i not in list:
#         list.append(i)
# print(i, end=" ")

#
# odd = []
# even = []
# def oe():
#     for i in range(0, 101):
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("even numbers:", even)
#     print("odd numbers:", odd)
#
# oe()

#
# x = int(input("enter num::"))
# def fac():
#     fact = 1
#     for i in range(1, x+1):
#         fact = fact * i
#     return fact
# print(fac())

# x = int(input('Enter num::'))
# def pn():
#     for i in range (2, x):
#         if x % i == 0:
#             print("not prime")
#             break
#     else:
#         print ("prime num")
# pn()
#
#
# lv = int(input('Enter num::'))
# hv = int(input('Enter num::'))
# for num in range(lv, hv+1):
#     if num>1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end =" ")

# x =input('Enter num::')
# def palin():
#     if x==x[::-1]:
#         print("palin")
#
#     else:
#         print("not")
# palin()


