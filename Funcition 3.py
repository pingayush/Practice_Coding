#When variable hoding 2 values its gets stored in form of tuple
def swap(a,b):
    c=a
    a=b
    b=c
    return(a,b)
p=swap()
print(p)

#default value
def swap(a=90,b=100):
    c=a
    a=b
    b=c
    return(a,b)
p=swap(200)
print(p)

#KeyWord Argument
def swap(a=90,b=100):
    return(a,b)
p=swap(b=200,a=900)
print(p)

