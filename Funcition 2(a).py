def greater(a,b,c):
    if(a>b):
        if(a>c):
            return(a)
        else:
            return(c)
    elif(b>c):
        return(b)

    else:
        return(c)


p=greater(10,2,30)
print(p)
