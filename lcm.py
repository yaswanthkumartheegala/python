print('enter two numbers to calculate LCM ')
a=int(input('enter the first number='))
b=int(input('enter the secound number='))
for m in range(1,a*b+1):
    if m%a==0 and m%b==0 :
        print('lcm of two numbers is =',m)
        break