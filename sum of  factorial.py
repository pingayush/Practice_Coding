n=int(input())
s=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    s=s+fact
print(s)
