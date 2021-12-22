print("aX^2 + bX + c = 0 \nGive the values of coefficient:")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = ((b**2)-(4*a*c))
print(d)
e=(d**0.5)


f= int(-b+e)
h= f//2*a

g = int(-b-e)
i= g//2*a
print(i+0j,"and",h+0j)

