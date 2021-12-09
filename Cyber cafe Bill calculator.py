hour=int(input())
minute=int(input())

if hour==5:
    amount=(200 + minute*1)
    print(amount)
if hour>=7:
    print("Hours Excedded")

elif hour>5:
    amount=int((hour*50 + minute*1) - 50)
    print(amount)
elif hour<7 :
    amount=(hour*50+ minute*1)
    print(amount)


