'''

e_id = 4325
print("employee id:", e_id)

e_id=input("Enter number::")
print("employee id:", e_id)

eid=100
# print("Employee details:", eid)
print("Employee details:", type(eid))
print("Employee details:", id(eid))

salary=1000
print("salary:", salary, type(salary))


m_bill = 234.45
print(m_bill)
print("m_bill:", m_bill, type(m_bill), id(m_bill))


x=232
# print("boolean value:", x, type(x), id(x))
# print("float value:", x, type(x))
print(float(x))
'''
# string introduction
'''
str1 = 'Hello World'
print(str1, id(str1[1]), (str1[2]), (str1[3]), str1[5], str1[6])
print("l mem location:", id(str1[2]), id(str1[3]), id(str1[9]))

ch = "1"
print(ch+"1",type(ch), id(ch))
print("addition of ch:", ch+"2")

ch=2.5
print(ch, type(ch), id(ch), ch+1)

for char in 'Hello World':
#    print(char, end="")
#    print(char[2])

x="Hello world"
x = [1, 2, 3, 4, 5, 6, 7, 8]
for(x[-1]) in x:
    print(x[-1])

message = 'HELLO-WORLD'
print("3rd index value:", message[3])
print("4thindex value:", message[5])
print("2 to 5:", message[2:5])
print("4 to 6:", message[4:6])
print("2 to 8:", message[2:8] )
print("0 to 10:", message[0:11])


str1 = 'Hello'
str2 = 'World'
print(str1 + str2, "python")
print("add str:", str1+str2)
print("add str:", str2+str1)
print("multipication:", 100*str1)

msg1 = 'HELLO-PYTHON'
print("H:", 'H'in msg1)
print("m:", 'm' in msg1)
print("H:", 'H' not in msg1)
print("O:", "O" in msg1)

str1 = 'HelloWorld'
print("max of str:", max(str1))
print("min of str:", min(str1))
'''
str1 = 'hello world'
# print("normal str:", str1)
# print("str after capitalize:", str1.capitalize())
print("str after capitalize:", str1.capitalize())


str1 = 'hello world'
str2 = 'hello world welcome'
print("normal stg:", str1 )
print("length after padding:", len(str1.center(28, '$')))
print("string after center function with width 28 & fillchar as $:", str1.center(28, '^'))
print("string after center function  with width 30 & fillchar as $:", str2.center(30, '^'))
print("string after center function with width 50 & fillchar as $:", str1.center(50, '^'))

str1 = 'helloworldhell'
print("slicing:",str1[0:10])
print("normal string: h", str1.count("h"))
print("normal string: o", str1.count("o"))
print("normal string:l", str1.count("l"))
print("normal string:d", str1.count('d'))


str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("encoded string:", str2)
print("decoded string:", str2.decode('UTF-8'))

mobile_no = 123456
print("before:", mobile_no, type(mobile_no))

mobile_no = str(mobile_no)
print("After:", mobile_no, type(mobile_no))