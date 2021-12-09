N=int(input("ENTER THE VALUE"))
k=N
rem=0
sum1=0
while(N!=0):
      rem=N%10
      sum1=sum1+pow(rem,3)
      N=N//10
if(sum1==k):
    print("ARMSTRONG")
else:
    print("NOT")
