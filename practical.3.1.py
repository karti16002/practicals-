a = int(input("Enter number of rows : "))
row=0
while row<a:
    star=row+1
    while star>0:
        print("* ",end="")
        star= star-1
    row=row+1
    print()


