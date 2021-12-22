n=int(input("Enter the number"))
if n>1:
    for x in range(2,n+1):
        if(n%x)==0:
             print("Not prime")
        else:
             print("Prime")
