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
--------------------------------------------------------------------------
 Dry run

 N    expansion               answer                  result

 153    1^3+5^3+3^3           1+125+27=153             yes

 1456   1^4+4^4+5^4+6^4       1+64+625+1296=1986       no

 1634   1^4+6^4+3^4+4^4       1+1296+81+256=1634       yes

 123     1^3+2^3+3^3           1+8+27=36               no
