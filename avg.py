count=0
total=0
value=float(input("enter a number: "))
while value!=0:
    total=total+value
    count=count+1
    value=float(input("enter the another number: "))
    if count==0:
        print("no value were entered.")
    else:
        average=total/count
        print("the average of those numbers is",average)