i=1
j=1
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end='')
-----------------------------------------

Dry Run

i=1
j=1

range of i belongs to(1,6) which means 1,2,3,4,5
range of j belongs to(1,i+1)which means

1
1,1+1---->1,2
1,2,2+1--------->1,2,3
1,2,3,3+1--------------->1,2,3,4
1,2,3,4,4+1----------------------->1,2,3,4,5
1,2,3,4,5+1------------------------------------>INVALID
