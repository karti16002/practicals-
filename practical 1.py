from math import sqrt

print("General Eqaution : ax^2 + bx + c = 0")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

D = b**2 - 4*a*c
# D should be positive


if D < 0:
	print("Root does not exist")
	exit()
    
D = sqrt(D)
R1 = (-b + D)/(2*a)
R2 = (-b - D)/(2*a)
print (R1,R2)