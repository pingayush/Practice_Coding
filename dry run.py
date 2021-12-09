fact=1
sum=0
for i in range(1,6,2):
    for j in range(1,i+1):
        fact=fact*j
        sum=sum+fact
        print(sum)
