'''
str1 = 'hello world'
print("capitalize:", str1.capitalize())
print("string after upper:", str1.upper())


str1 = 'hello world'
print("string:", str1.capitalize())
print("string:", str1.upper())
print("no of e's in the string: h", str1.count('h'))
print("no os l's in the sring:l", str1.count('l'))

str1 = 'hello world'
str2 = str1.encode('UTF-8')
print("Encoded string:", str2)
print("Decoded string:", str2)
print("If the normal string ends with id or not:", str1.endswith("id", 5, 12))
print("If the normal string ends with ld or not:", str1.endswith("ld", 5, 11))
print("If the normal string ends with lo or not:", str1.endswith("lo", 3, 5))

str1 = 'hello world'
print("expand tabs:", str1.expandtabs(26))
print("without expand tabs:", str1)

str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"
print("index of ash is present in chesapeake ripper between index 0 & 21:", str1.find("ash", 0, 21))
print("index of ter is present in Hannibal\tLecter between index 0 & 16:", str2.find("ter", 0, 16))
print("Index of pea is present in the chesapeake ripper between index 0 & 20:", str1.index('pea', 0, 20))

str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"
str3 = "Aug231994"
print("Aug231991 is aplhanumeric:", str3.isalnum())
print("Hannibal\tLecter is aplhanumeric:", str2.isalnum())
print("chesapeake ripper is aphanumeric:", str1.isalnum())
print("chesapeake ripper contains only alphabets:", str1.isalpha())
print("chesapeakeripper is contains only alphabets:", str1.isalpha())
print("ake contains only aplhabets:", str1.isalpha())



num_str1 = "23081994"
substr1 = "ake"
print("ake contains only alphabets:",num_str1.isdigit())
print("23081)