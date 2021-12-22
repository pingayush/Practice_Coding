n=int(input("Enter the value"))
fact=1
sum1=0
for i in range(1,n+1):
    fact=fact*i
    if(i%2==0):
       sum1=(sum1-(i/fact))
    else:
       sum1=(sum1+(i/fact))
print(sum1)
