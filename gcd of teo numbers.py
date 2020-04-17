a=int(input('enter the first number='))
b=int(input('enter the secound number='))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
    print('hcf is =',b)




