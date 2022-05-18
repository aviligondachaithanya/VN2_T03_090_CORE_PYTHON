'''
## 1.check given word is palindrome or not
# Method:1
def palindrome(x):
    return x == x [::-1]

x = "malayalam"
res = palindrome(x)
if res:
    print('yes')
else:
    print('no')

x = "malayalam"
c = ""
for i in x:
    c = i+c
if (x==):
    print('yes')
else:
    print('no')

# Method:2
x = "malayalam"
c = ""
for i in x:
    c = i+c
if (x==c):
    print('yes')
else:
    print('no')

#Method:3
p = ["happy", "new", "year"]
result = list(filter(lambda x: (x == "".join(reversed(x))), p))
print(result)
'''
## 2.print even and odd numbers
# Method:1
def even_odd (num):
    if num % 2==0:
        return even
    elif num % 2 !=0:
        return even
num = int(input("Enter any num::"))
result = even_odd(num)
print(result)

#Method:2
num = int(input("Enter any num::"))
if num % 2 == 0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))

#Method:3
num = int(input("Enter any num::"))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


## 3.print prime numbers
#Method:1
for num in range(1, 1000, 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=" ")

# Method:2
number = int(input("Enter any number:"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number, "is not prime number")
            break
    else:
            print(number, "is prime number")

## 4.Factorial
#Method:1
def factorial(a):
    fact = 1
    for p in range(a, 0, -1):
        fact = factorial * p
    return fact
n = int(input("Enter a num:"))
res = factorial(n)
print("factorial of 'n', ''is", res)

# Method:2
fact = 1
num = int(input("Enter a num::"))
ord = num
while num > 0:
    fact = fact * num
    num = num - 1
print("factorial of",  'ord', 'is', fact

#Method:3
num = 5
if num < 0:
    print("Factorial Does not exist for negative num")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial=factorial+i
    print("factorial of", num, "is" factorial)
# Not working

## 5.convert list/tuple/set to list/tuple/set




## 6.find cube/square of a number
#Method:1
num = int(input("Enter any num:"))
square = num * num
print("Given num square:", square)
res = square*num
print("Given num cube:", res)

#Method:2
cubes=[]
for i in range(11):
    cubes.append(i**3)
print(cubes)

square=[]
for i in range(5):
    square.append(i*2)
print(square)

#Method:3
def square (num):
    return (num*num)

def cube (num):
    return (num*num*num)

number = int (input("Enter any num:"))
print( "square of {0} is {1}".format(number, square(number)))
print ("cube of {0} is {1}".format(number, cube(number)))

#Method:4
nums = [1, 2, 3, 4, 5, 6]
square = list(map(lambda x:x**2, nums))
print(square)
cube = list(map(lambda x:x**3, nums))
print(cube)

