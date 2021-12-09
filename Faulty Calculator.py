# 45*3 = 555 , 56+9 = 77 , 56/6 = 4

# It is the calculator that will give all calculation correct except the above calculations.
i=21
while(i>0):


    print("Welcome To Python Calculator")
    print("Calculation No.1")

    print(" First no. ")
    a = int(input())
    print("OPERATION :  (+       -           *       / ) ")

    b = input()

    print("second no.")
    c = int(input())

    if b == "add" and a == 56 and c == 9:
        print('RESULT ')

        print(77)


    elif b == "add" and a == 9 and c == 56:
        print('RESULT')

        print(77)

    elif b == "+":
        print('RESULT')

        print(int((a + c)))
    elif b == "-":
        print('RESULT')

        print(a - c)
    elif b == "*" and a == 45 and c == 3:
        print('RESULT')

        print(555)
    elif b == "*" and a == 3 and c == 45:
        print('RESULT')

        print(555)
    elif b == "*":
        print('RESULT')
        print(a * c)
    elif b == "/" and a == 56 and c == 6:
        print('RESULT')

        print(4)
    elif b == "/":
        print('RESULT')

        print(a / c)
    print("\n\n NEXT Calcuation \n\n")





    






































