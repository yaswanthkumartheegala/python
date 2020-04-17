print("enter the numbers=")
a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
if a>b and a>c:
    print(a,"is s largest")
elif b>a and b>c:
    print(b,"is a largest")
else:
    print(c,"is largest")