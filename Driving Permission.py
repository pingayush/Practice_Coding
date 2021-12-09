i=2
while(i>0):
    print("What is your Name ?")
    name = str(input())
    print("Age")
    age = int(input())
    if age >= 100:
        print( "Invalid Age\n\nTRY Again\n")
        break
    if age > 18:
        print(name,"you can Drive")
    elif age == 18:
            print(name,"you have to give a test after passing it you Can get Your DL.")
    else:
        print(name,"You Cannot drive")






