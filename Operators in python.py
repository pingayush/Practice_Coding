"""
Arithmetic operators
Assingment operators
comparison operators
logical operators
identity operators
membership operators
bitwise operators
"""
# 1. Arithmetic operators
print("Arithmetic operators")
print("1 + 2 equals to", 1+2)
print("5-2 equals to ", 5-2)
print("3*2 equals to",3*2)
print("6/2 equals to",6/2)
print("5//2 equals to",5//2) #this // operator gives only integer value.
print("3**3 equals to",3**3) #this ** operators used to raise power on any no.
print("6%2 equals to", 6%2) # thi % operator gives remainder.

# 2.Assingment operators
print("Assingment operators") #it means to store any numeric value in any varible
x = 6
print(x)
y = x + 2
print(y)

# 3. comparison operators
print("comparison operators")
i = 2
print( i ==3)
print(i>1)
print(i<5)
print(i!=2) # (! + = ) = !=
# 4. logical operators
print("logical operators")
a = True
b = False
print(a and b)
print(a or b)
print(a and a)
print(b and a)
print(b and b)

# 5. identity operators

print("identity operators")
c = 5
d = 7
print(c is d)
print(c is not d)
print(1 is 1)
print(4 is not 2)

# 6. membership operators
list = [3,1,2,5,6,7,8,9,10,11,123]
print(21 in list)
