print("Enter 1st no.")
a = int(input())
print("Enter 2nd no")
b = int(input())
print("Enter 3rd no.")
c = int(input())

d = str(a)+str(b)+str(c)

e=str((a*a*a) +(b*b*b)+(c*c*c))

if d==e:
    print(d,":Is an Armstrong number")
else:
    print(d ,":Not an Armstrong number")

