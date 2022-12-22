a = int(input("Enter a number "))

if a<=1:
    print("invalid output")
    exit()

def checkprime(x):
    start=0
    for i in range(2,x):
        if x%i==0:
            start=1
    if start==0:
        return True
    else:
        return False
i=2
while i<=a:
    if checkprime(i):
        print(i)
    i=i+1






       

 