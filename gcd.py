x=int(input('enter the number x = '))
y=int(input('enter the number y = '))
if x>y:
   z=x%y
else:
    z=y%x
    for i in range(1,z+1):
        if( (x%i==0) and (y%i==0)):
            print('the gcd is i',i)
        else:
            gcd=i


