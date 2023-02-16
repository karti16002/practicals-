s = input("enter a string: ")
a= input("enter a character to remove: ")
i = s.index(a)
print(s[:i]+s[i+1:])