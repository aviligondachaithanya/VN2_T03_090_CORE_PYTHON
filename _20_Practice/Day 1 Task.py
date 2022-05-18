# 1.Parameters
def square (num):
    return (num*num)

def cube (num):
    return (num*num*num)

number = int (input("Enter any num:"))
print( "square of {0} is {1}".format(number, square(number)))
print ("cube of {0} is {1}".format(number, cube(number)))

# 2.Return Statement
#2.1
def sum (n1,n2):
    result = n1 + n2
    print("Addition:", result)

sum(n1=10, n2=30)

# 2.2
def factorial(a):
    fact = 1
    for p in range(a, 0, -1):
        fact = factorial * p
    return fact
n = int(input("Enter a num:"))
res = factorial(n)
print("factorial of 'n', ''is", res)

#2.3
def even_odd (num):
    if num % 2==0:
        return 'even'
    elif num % 2!=0:
        return 'odd'
num = int(input("Enter any num::"))
result = even_odd(num)
print(result)

#3. Returning multiple values from a function
def operation (n1=10, n2=30):
    x = n1 + n2
    y = n1 - n2
    return x,y
print("positional arguments:", operation(10, 30))
print("Defalut arguments:", operation(10, 30))
print("Keyword arguments:", operation(n2=10, n1=20))

# 1.Table
def table (num):
    for i in range(1, 11):
        print (num, 'x', i, '=', num*i)

n = int(input("Enter any num:"))
table(n)

#2&3. List,set,Tuple add and mulitply
def list(x):
    total = 0
    total2 = 1
    for i in x:
        total = total+i
        total2 = total2*i
    return total, total2
x=[1, 2, 3, 4, 5, 6]
solution=list(x)
print("sum and multiplication of list:", solution)

def set(x):
    total = 0
    total2 = 1
    for i in x:
        total = total+i
        total2 = total2*i
    return total, total2

x={1, 2, 3, 4, 5, 6, 7, 8}
solution=set(x)
print("sum and multiplication of set:", solution)


def tuple(x):
    total = 0
    total2 = 1
    for i in x:
        total = total + i
        total2 = total2 * i
    return total, total2
x=(1, 2, 3, 4, 5, 6, 7, 8)
solution=tuple(x)
print("sum and multiplication of tuple:", solution)

## 5.Accepts a string and calcualte the number of uppercase and lowercase letters
string = "Chaithanya AVILIGONDA"
def letters (string):
    lc=uc=0
    for i in string:
        if i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
    print("upper case:", uc)
    print("lower case:", lc)
letters(string)

##6.Take a list and return a list with unique elements of the first list

def unique(elements):
    result = []
    for num in elements:
        if num not in result:
            result.append(num)
    return result
elements = [11, 12, 13, 13, 14, 15, 15, 11]
print(unique(elements))


## 7.print given pascals triangle
def solve(n):
    for i in range(n+1):
        for j in range (n-i):
            #print(" ", end="")

        c = 1
        for j in range (1, i+1):
            print(" ", c, sep="", end="")
            c = c * (i - j)//j
        print()

n = 5
solve(n)


## 8.Function to check whether a string is a palindrome or not
def palindrome(x):
    return x == x [::-1]

x = "malayalam"
res = palindrome(x)
if res:
    print('yes')
else:
    print('no')


# 9.Check whether a number is in a given range
def test_range(n):
    if n in range(0, 1000):
        print("Number is in the range", str(n))
    else:
        print("Number is out of range")
test_range(0)
