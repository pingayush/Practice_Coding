Odd_Sum=0
Even_Sum=0
list=[]

a=int(input("ENTER THE ELEMENTS IN THE LIST"))
for j in range(0,a+1):
    if list(j)%2 ==0:
        Even_Sum = Even_Sum + list[j]
    else:
        Odd_Sum = Odd_Sum + list[j]

print("The Sum of Even Numbers in list = ", Even_Sum)
print("The Sum of Odd Numbers in list = ", Odd_Sum)

