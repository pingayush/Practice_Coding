a=input("Name ")
b= int(input("Account Number "))
c=input("Account type ")
d= int(input("Deposited amount "))
e=int(input("Withdrawn amount "))
f=int(d-e)

if c=="Savings":
    if f<1000:
        print("Balance ",(f + d*0.009) -(0.025*f +5))
        print("Penalty Charged : 5 ")
        print("Service charged ",f*0.025)
        print("Interest Credited ",d*0.009)
    elif f>=1000:
        print("Balance ", (f + d * 0.009) - (0.025 * f ))
        print("Penalty Charged : 0 ")
        print("Service charged ", f * 0.025)
        print("Interest Credited ", d * 0.009)
elif c=="Current":
    if f<5000:
        print("Balance ",(f + d*0.009) -(0.025*f +25))
        print("Penalty Charged : 25 ")
        print("Service charged ",f*0.025)
        print("Interest Credited ",d*0.009)
    elif f >= 5000:
        print("Balance ", (f + d * 0.009) - (0.025 * f ))
        print("Penalty Charged : 0 ")
        print("Service charged ", f * 0.025)
        print("Interest Credited ", d * 0.009)


