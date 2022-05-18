'''

s1 = {1, 2, 2, 2, 2, 4, 3, 5, 2, 7, 6}
print(set(s1))

s1 = {1, 1, 3, True, 'Hello', (1, 2, 3)}
print(s1)

s1 = {1, 2, 4, True, 'Hello', 'Python', (1, 2, 3)}
for each in s1:
    print(each, end=" ")

s1 = {1, 4, 5, 7, 2, 6, 3}
s1.add(111)
print(s1)
s1.discard(4)
print(s1)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1&s2)
print(s1-s2)
print(s2-s1)


setA = set(["Mon","Tue","Wed"])
setB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
subsetRes= setA<=setB
SupersetRes= setB>=setA
#print("SetA is subset of SetB:", SubSetRes)
print("SetB is superset of SetA:", SupersetRes)
'''

