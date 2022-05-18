
## 1.Length of string
# Method:1
# x = "Happy new year"
# print("length of string:", len(x))

#Method:2
def length (x):
    counter = 0
    for i in x:
        counter += 1
    return counter
x = "Happy new year"
print(length(x))

#Method:3
x = input("Enter the string:")
c = 0
for i in x:
    c += 1
print(c)


'''
## 2.Count characters in string
#Method:1
x = "Happy new year"
print("number of p's in the string:", x.count('p', 0, len(x))

#Method:2
string = input("Enter the string:")
char = input("Enter any char in the string:")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count+1
print("num of time:", "char," "has occured:", count)

#Method:3
count = 0
string = "happy new year"
char = "y"
for i in string:
    if i == char:
        count += 1
print(count)

#Method:4
def count(x):
    x="Happy new year"
    count=0
    for i in x:
        if x=="a":
            count += 1
print(count(x))
'''
'''
## 3.String slicing
#Method:1
x = "Happy new year"
print(len(x))
print(x[0:4]
print(x[5:9])

#Method:2
for i in x[5:9]:
    print(i, end=" ")
'''
## 4.Replace first occurance character
#Method:1
x = "Happy new year"
print("Replace a with @ Happy new year in only once:", x.replace("a", "@", 1))

#Method:2
x = "Happy new year"
def replace (x, char, index):
    return x[:index] + char + x[index +1:]
    x[index +1:]

res = replace(x, "@", 1)
print(res)

## 5. Swapping chars in string
#Method:1
x = "Happy new year"
print("Swapping the case of Happy new year:", x.swapcase())

#Method:2
def swapping(x):
    x = list(x)
    for i in range (0, len(x)-1, -2):
        x[i], x[i+1], = x[i+1], x[i]
        return " ".join(x)

x = "Happy new year"
print(swapping(x))

##6.Append chars to string at end
#Method:1
first = "welcome"
second = "VN2"
first += second
print("After adding:" + first)

#Method:2
first = "welcome"
second = "VN2"
print(" ".join([first, second]))

#Method:3
first = "welcome"
second = "VN2"
result="{} {}".format(first, second)
print(result)

#Method:4
first = "welcome"
second = "VN2"
print("% s % s " %(first, second))

## 7.Substring replacement
#Method:1
x = "Happy new year"
print(x.replace("Happy", "H@ppy"))


## 8.Length of longest string in python
#Method:1
x = "Happy new year"
print("max length of string:", max(x))

## 9.nth index character from string
#Method:1
x = "Happy new year"
print("7th charcter of a string:", x[7])

# Method:2
x = "Happy new year"
for i in x[7]:
    print(i)

# Method:3
def find_all (a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

list(find_all("Happy new", "year"))
#Not working

## 10.First last chars swapping
x = "Happy new year"
print("afyer swapping:", x.swapcase())

## 11. Remove odd index values
x= "Happy new year"
y= " "
for i in range (len(x)):
    if (i % 2==0):
        y = y+x[i]
print("original string:", x)
print("Final string:", y)


## 12. Count words in a string
# Method:1
x = "Happy, new, year"
res = len(x.split())
print(" num of words:" + str(res))

# Method:2
def count_words (string):
    string1 = string.strip()
    count = 1
    for i in string1:
        if i ==" ":
            count +=1
    return count
string= "happy, new, year"
print("'{}'".format(string), "has total words:", count_words(string))





# Upper lower case of a string
x = "Happy new year"
#print("after upper case:", x.upper())
print("after lower case:", x.lower())


# Last part of string
x = "Happy new year"
last_word = x[-3:]
print("last part:", last_word )

# Convert a given string to all uppercase
x = "Happy new year"
print("convert to uppercase:", x.upper())


# program to remove a new line in Python
x = "Happy new year 2022"
print("after removing:", x.rstrip("2022"))

# program to check whether a string starts with specified characters
x = "Happy new year"
print("happy is starts are not:", x.startswith('Happy'))

# to set the indentation of the first line...?
# To indent the first line of a paragraph, put your cursor at the beginning of the paragraph and press the
# tab key.When you press Enter to start the next paragraph, its first line will be indented.

# to print the following floating numbers upto 2 decimal places
x = 3.1415926
print("with two float numbers: ""{:.2f}".format(x))

# print the following floating numbers upto 2 decimal places with a sign
x = 12.34567890
print("with floats and symbol:"+"{:+.2f}".format(x)

# to display a number with a comma separator
x = 1234567890
y = "{:,}".format(x)
print(y)

# to format a number with a percentage
x = 0.123
y="{:.1%}".format(x)
print(y)

# to count occurrences of a substring in a string
x  = "Happy new year 2022"
print("after replacing year:", x.replace("2022","welcome 2023"))


# count repeated characters in a string
x  = "Happy new year 2022"
#print("Duplicate characters in a given string: ")
for i in range(0, len(x)):
    count=1
    for j in range (i+1, len(x)):
        if (x[i]==x[i] and x[i] != " "):
            count = count+1
            x = x[:j]+'0'+x[j + 1:]
    if ( count >1 and x[i] != '0'):
        print(x[i], "-", count)

# print the index of the character in a string
x  = "Happy new year"
print("index of specific character:", x.find("H"))

# convert a string in a list
def convert (x):
    res = list (x.split(" "))
    return res

x = "Happy new year"
print((convert(x)))



# swap comma and dot in a string
x = "Happy new year"
maketrans = x.maketrans
x=("after swapping:", x.maketrans(",.", ".,"))
print(x)

# count and display the vowels of a given text

# remove spaces from a given string
def remove(x):
    return "".join(x.split())

x = "H a p p y n e w y e a r"
print(remove(x))


# move spaces to the front of a given string

# capitalize first and last letters of each word of a given string
String = "Happy new year"
String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
print(String)


# remove leading zeros from an IP address
# def IP(ip):
#    zeroip = ".".join([str(int(i)) for i in ip.split(".")])
#    return zeroip
#
# ip =input("Enter the IP address ::>")
# print("New Ip Address ::>", IP(ip))


import _01_numbers
hostname = _01_numbers._2_bool.py()
IPAddr = _01_numbers._2_bool.py(_2_bool.py)
print("Your Computer Name is:" + _2_bool.py)
print("Your Computer IP Address is:" + IPAddr)

'''





