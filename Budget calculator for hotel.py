t=int(input("No. of tabels : "))
ct=int(input("Cost of one table : "))
c=int(input("No. of chairs : "))
cc=int(input("Cost of one chair : "))
w=int(input("No. of hours worked : "))
wph=int(input("Wages per hour : "))

CT = ct*t
CC = cc*c
LC = wph*w
Budget_for_Hotel = (int(CT) + int(CC) +int(LC))
print("Budget for Hotel : ",Budget_for_Hotel)
