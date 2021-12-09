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
================================================
Dry Run:
let 'p' be variable
p=greater(10,2,30)

Example-1:
    greatest(10,2,30)
    10>2 --------------------------------> Loop-1 will Run
    10<30 ---------------------------------------> Loop-1(a) Failed
              *Loop-1(b) will Run*
    Hence:
        p will be printed as 30

