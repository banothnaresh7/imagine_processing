def fibbonaci():
    a=int(input())
    b=int(input())
    for i in range(10):
        c=a+b
        a=b
        b=c
        print (c)

fibbonaci()
