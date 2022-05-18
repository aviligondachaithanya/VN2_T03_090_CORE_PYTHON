'''
# sum of elements
x = [11, 12, 13, 14, 15]
total = 0
for i in range(0, len(x)):
    total = total + x[i]
    print("sum of all:", total, end=" ")


# Mulitply of elements

# Largest number from list
x = [11, 12, 13, 14, 15]
print("Largest num:", max(x))

# Smallest number from list
x = [11, 12, 13, 14, 15]
print("smallest num:", min(x))


# Remove duplicates
x = [11, 12, 13, 14, 15, 11, 13, 15, 8888]
list = []
for i in x:
    if i not in list:
        list.append(i)
print("After removing duplicates:", ''+str(list))


# Check list is empty or not
def enquiry (x):
    if len(x) == 0:
        return 0
    else:
        return 1

x = [ ]
if enquiry(x):
    print("Non_zero")
else:
    print("zero")


# Clone or copy
x = [11, 12, 13, 14, 15, 11, 13, 15, 8888]
print("after copy:", x.copy())


# Find common element from 2 lists
def common_element(x, y):
    x = set(x)
    y = set(y)
    if (x & y):
        print(x & y)
    else:
        print("No common elements")

x = [11, 12, 13, 14, 15, 11, 13, 15, 8888]
y = [11, 12, 13, 14, 99, 88, 999]
common_element(x, y)


# Remove specified index from list and print
x = [11, 12, 13, 14, 99, 88, 999]
print("after removing element:", x.pop())
print(x)
print("after removing element:", x.remove(88))
print(x)


# Remove even elements and print

x = [11, 12, 13, 14, 99, 88, 999]
print("list items =", x)
for i in x:
    if (i % 2==0):
        x.remove(i)
print("List items after removing even elements:", x)


# Shuffle list and print
import random
x = [11, 12, 13, 14, 99, 88, 999]
random.shuffle(x)
print(x)


# Difference betweeen 2 lists
x = [11, 12, 13, 14, 15, 8888]
y = [11, 12, 13, 14, 99, 88, 999]
difference1=[]
for element in x:
    if element not in y:
        difference1.append(element)
print(difference1)

difference2=[]
for element in y:
    if element not in x:
        difference2.append(element)
print(difference2)

differences=difference1+difference2
print(differences)


# To access index of list
x = [11, 12, 13, 14, 15, 8888]
print("3rd index position:", x[2])


# List of characters into string
def split (x):
    return [char for char in x]

x = "chaithanya"
print(split(x))

# Finding index of an item in specified
x = ['c', 'h', 'a', 'i', 't', 'h', 'a', 'n', 'y', 'a']
print("index position of 'a':", x.index('a'))


# Flatten a shallow
from itertools import chain

x = [[11, 12, 13], [14, 15, 8888], [16, 17, 18], [111,222,333],[444,555,666]]
res = sorted(chain(*x))
print(res)

# Append a list to second list
x = [11, 12, 13, 14, 15, 8888]
y = ['welcome', 'vn2']
x.append(y)
print("after append:", x)


# Select an item randomly
import random
x = [11, 12, 13, 14, 15, 8888]
print(random.choice(x))

# Check circularly identical in two lists

# Finding a second smallest number

def find (x):
    length=len(x)
    x.sort()
    print("Second smallest num:", x[1])

x = [11, 12, 13, 14, 15, 8888]
second smallest = find(x)

# Finding a second largest number
def find(x):
    length=len(x)
    x.sort()
    print("second smallest num:", x[-2])

x = [11, 12, 13, 14, 15, 8888]
largest=find(x)

# Get unique values
def unique (x):
    unique_list = []
    for i in x:
        if i not in unique_list:
            unique_list.append(x)
    for i in unique_list:
        print(i)

x = [11, 12, 13, 14, 15, 8888]
print("unique values from x is")
unique(x)
y = [1, 3, 4, 5, 9, 8, 99]
print("unique values from y is")
unique(y)


# Frequency of elements

# Counting number elements with in a specified range

# Check a list contains sublist
test_list = [11, 12, 13, 14, 15, 16, [17, 18, 19]]
sub_list = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0
if (all(x in test_list for x in sub_list)):
    count = 1
if (count):
    print("(list is subset of other")
else:
    print("list is not subset of other")
'''

# Generate all sublists

# Printing elements in ascending order
x = [11, 12, 77, 88, 111, 121, 13, 14, 15, 8888]
x.sort()
print(x)

# Create a list by concatenating a given list which range goes from 1 to n
x = [11, 12, 13, 14, 15, 8888]
y = [11, 12, 13, 14, 99, 88, 999]
numbers = x+y
print("concatenated list: \n \n" +str(numbers))

# Variable unique identification number

# Finding common items from two lists

def common_element(x, y):
    x = set(x)
    y = set(y)
    if (x & y):
        print(x & y)
    else:
        print("No common elements")

x = [11, 12, 13, 14, 15, 11, 13, 15, 8888]
y = [11, 12, 13, 14, 99, 88, 999]
common_element(x, y)

# Change the position of every nth value with (n+1)th value
def rightrotate(lists, num):
    output_list =







