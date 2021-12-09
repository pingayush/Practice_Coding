m=int(input())
n=[]
n.append(0)
n.append(1)
if(m==2):
    print('0 1')
elif(m==1):
    print('0')
else:
    for i in range(2,m):
        m.append((m[i-1]+m[i-2]))
for i in range(len(1)):
    print(m[i],end=' ')
