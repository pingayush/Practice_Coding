count=0
for i in range(2,11):
    print()
    for j in range(1,i+1):
         if(i%j==0):
            count=count+1
    if(count==2):
        print("PRIME",i)
    else:
        print("NOT PRIME",i)
    count=0
