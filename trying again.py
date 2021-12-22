n=int(input("Enter a number: "))
s=0
for i in range(1,n+1):
    s=s+(i//2)
print(s)


---------------------------------------
Dry run

i is in range (1,n+1) therefore i belongs from 1 to n
s=0
and s=s+(i//2)
therefore
s=1/2
+
s=2/2
.
.
.
.
.
.
.
.
.
.
.
.
+
s=n/2
hence the
Answer is 1/2+2/2+3/2+4/2+...........+n/2
