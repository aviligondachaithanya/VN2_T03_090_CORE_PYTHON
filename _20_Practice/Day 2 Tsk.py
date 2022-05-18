#
# class leap:
#     def new(self,x):
#         if x % 4 == 0 and x % 100 != 0:
#             retun = 1
#         elif x % 400 == 0:
#             rerurn = 1
# print("Enter year:", end= "")
# x = int(input())
#
# ob1 = leap()
# ob2 = ob1.new(x)
# if ob2 == 1:
#     print("Leap year")
# else:
#     print("Not a leap year")


# define a method for checking number is Armstrong or not
# class Amstrong:
#     def __init__(self, number):
#         self.num = number
#     def isArmstrong(self):
#         temp = self.num
#         res = 0
#         while (temp != 0):
#             rem = temp % 10
#             res += rem ** 3
#             temp //= 10
#         if self.num == res:
#             print(self.num, "is Armstrong")
#         else:
#             print(self.num, "is not Armstrong")
# if __name__ == "__main__":
#     num = 153
#     a= Amstrong(num)
#     a.isArmstrong()

## Calculator

# class cal():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
#     def sub(self):
#         return self.a-self.b
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# obj=cal(a,b)
# choice=1
# while choice!=0:
#     print("0. Exit")
#     print("1. Add")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = int(input("Enter choice: "))
#     if choice == 1:
#         print("Result: ", obj.add())
#     elif choice == 2:
#         print("Result: ", obj.sub())
#     elif choice == 3:
#         print("Result: ", obj.mul())
#     elif choice == 4:
#         print("Result: ", round(obj.div(), 2))
#     elif choice == 0:
#         print("Exiting!")
#     else:
#         print("Invalid choice!!")
#
# print()


## Roman

# class Roman(object):
#    def romanToInt(self, s):
#       roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
#       i = 0
#       num = 0
#       while i < len(s):
#          if i+1<len(s) and s[i:i+2] in roman:
#             num+=roman[s[i:i+2]]
#             i+=2
#          else:
#             num+=roman[s[i]]
#             i+=1
#       return num
# ob1 = Roman()
# print(ob1.romanToInt("III"))
# print(ob1.romanToInt("X"))