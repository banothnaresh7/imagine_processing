def fibbonaci():
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    for i in range(10):
        c=a+b
        a=b
        b=c
        print (c)

fibbonaci()
