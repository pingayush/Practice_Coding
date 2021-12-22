i=1
j=1
for i in range(5,0,-1):
    print()
    for j in range(1,6):
        print(i,end='')
----------------------------------------------

Dry Run

Range of i is (5,0) which means that i=5,4,3,2,1 as 0 is excluded in the range
Range of j is (1,6) which means that j=1,2,3,4,5 as 6 is excluded in the range

Now i is row and j is the column here

therefore

for print(i,end='')                            #(,end='') means it will print in the same line
55555 as i=5, j=1
44444 as i=4, j=2
33333 as i=3, j=3
22222 as i=2, j=4
11111 as i=1, j=5
