P=int(input('enter the principal:'))
R=float(input('enter the rate :'))
T=float(input('enter the time :'))
Si=(P*R*T)/100
Ci=P*((1+R/100)**T)-P
print('simple intrest is :',Si)
print('compound interest is :',Ci)