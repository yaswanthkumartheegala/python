def squaresum(n):
    n=int(input('enter the n value:'))
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i)
        return sm
   
    print(squaresum(n))