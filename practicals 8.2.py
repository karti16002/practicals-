'''b = input("enter a character ")
if b>='a'and b<='z':
    print(b,"is a lowercase alphabet")
elif b>='A' and b<='Z':
    print(b,"is a uppercase alphabet")
elif b>='0' and b<='9':
    print(b,"is a number")
else:
    print(b,"special character")'''
c = input('Enter a character : ')[0]

if (c >= '0' and c <= '9'):
	print("number")
elif (c >= 'a' and c <='z'):
	print("alphabet")
elif (c >= 'A' and c <='Z'):
	print("alphabet")
else:
	print("Special character")
