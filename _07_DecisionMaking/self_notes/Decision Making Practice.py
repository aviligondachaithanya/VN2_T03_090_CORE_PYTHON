'''

x = 25
print("x = 25")

me = "chay"
print(me=="chay")
print(me=="chai")

chay = "aviligonda"
print(chay=="aviligonda")
print(chay=="chaithu")

chay = "aviligonda"
print(chay=="aviligondaa")

me = "xyz"
if(me == "xyz"):
    print("welcome to vn2")
else:
    print("join to vn2")

me= "it"
if(me=="it"):
    print("join to vn2")
    if(me=="itt"):
        print("join python")


chay = "python"
if(chay=="python"):
    print("welcome to python")

chay = "vn2"
if(chay == "vn2") : print("join to vn2.")

chay = "vn2"
print("join to vn2") if (me=="vn2") else print("join to python")


chay = "vn2"
if(chay==" "):
    print("if condition fails")
if None:
    print("checking none exec:")
if not None:
    print("checking not  none value:")

if 10-20:
    ("print ops subractions 2 ")

if 10>20:
    ("comparins ops 1 ")

if 10+20 > 5+12:
    ("comparions ops 2")


x=12
print(x,type(x))

# dynamic way of giving input value "12"
x=input ("enter number:")

# dynamic way of input value int("11")
x=input ("enter number:")

# x = 15
if x>=10:
    print("two digit number")

# x =1
if x<10:
    print("one digit number")

print("-------end of the program--------")

# conditions:
# True ===> True, nonzero, non none
# False ====> false, zero, none

if 10>5:
    print("only enter values below 10")

if 10%2:
    print("division result is zero "

#required: check whether given number is -#postive
    # negative

#num=10
num = int(input("Enter any number:  "))
if num > 0:
    print("number is postive")
elif num < 0:
    print("number is negative")
else num==0:
    print("neither pos.nor neg")


rows=int(input=("enter num of rows:"))
for i in range(0, rows+1):
    for n in range(i):
        print(i,end="")
    print()

num=1
count=0
while num<100:
    if num%2==0:
        print(num, end=" ")
        count +=1
        if count==5:
            break
    num +=1


num=1
count=0
while num<50:
    if num%5 == 0:
        print(num , end=" ")
        count += 1


x="Happy new year"
def reverse(x):
    str=" "
    for i in x:
        str = i + str
    return str
print("Reverse of string :",reverse(x))



string = "Happy New Year"
x = string[::-1]
print(x)


x = "Happy New Year"
for i in  x[::-1]:
    print(i, end=" ")

def chu(p):
   chu=p[::-1]
   print(chu)
chu("happy new year")



x=[11, 12, 13, 14, 15]
(x.reverse())
print(x)

'''

x=[11, 12, 13, 14, 15]
x[::-1]
print(x)

















    
    
    
    

















