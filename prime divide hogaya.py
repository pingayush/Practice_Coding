N=int(input("ENTER THE VALUE"))
dividehogya=False
if N==2:
    print("Prime")
else:
    for i in range(2,N):
       if(N%i==0):
           dividehogya=True
           break;
if(dividehogya==False):
    print("PRIME")
else:
    print("NOT PRIME")
-------------------------------------------

Dry Run


N   i       N%i   Answer             True/False    Result

2                                                  Prime

3   (2,3)   3%2   Not equal to 0        False

4   (2,4)   4%2   Equal to 0            True       Not Prime

5   (2,5)   5%2   Not equal to 0
            5%3   Not equal to 0        False      Prime
            5%4   Not equal to 0
            
