for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i,1,-1):
        print(k-1,end='')
---------------------------------------

Dry Run

Range of i belong in (1,6) that is 1,2,3,4,5 where 6 is excluded
Range of j belong in (1,i+1) that is (1,6) which is 1,2,3,4,5 where 6 is excluded
Range of k belongs in (i,1,-1) that is (5,1) which is 5,4,3,2 where 1 is excluded

1                    i=1,j=1,k=0
121                  i=2,j=2,k=1
12321                i=3,j=3,k=2
1234321              1=4,j=4,k=3
123454321            1=5,j=5,k=4
