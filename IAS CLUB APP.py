i=21
count=0

while(i>0):
    print("WELCOME TO IAS CLUB APP")
    print("        ______________ ")
    print("              |                     / \                    ------- ")
    print("              |                    /___\                   \        ")
    print("              |                   /     \                   \       ")
    print( "       ---------------   ..      /       \    ..      _______\ \n\n\n\nIf you have already registered with us type :SIGN IN \n\nIf you are new here Type: SIGN UP")

    a = (input())
    list1 = [["Ayush", 100], ["Piyush", 200], ["Neeraj", 300], ["Shraddha", 400]]
    dict1 = dict(list1)


    if a == "SIGN IN":
        print("USERNAME")
        b = str(input())
        print("PASSWORD")
        c = int(input())
        if c==dict1[b]:
            print("WELCOME",b)
            print("       ______________ ")
            print("              |                      / \                    ------- ")
            print("              |                     /___\                   \        ")
            print("              |                    /     \                   \       ")
            print("       ---------------   ..       /       \    ..      _______\       ")

            print("IAS CLUB\n\n1.Dashboard\n2.Profile\n3.Services\n4.Courses\n5.HELP\n\nWhat you wish to open")
            d = input()

            if d == "Profile":
                print("1.View Profile pic \n2.Edit Profile\n3.Privacy and Security \n4.Language ")
                z= input('What you wish to open \n')
                if z== "Edit Profile":
                    print("\n\n**Coming Soon**\n\n")
                    break
                else:


                    break
            elif d == "Services":
                print("1.Register for UPSC Exam Course\n2.Notes\n3.E-Books\n4.Join Mock Test\n5.Previous Years Paper ")
            elif d== "Courses":
                print("\n\n**Coming Soon**\n\n")
                break
        elif c!=dict1[b]:
            print("Invalid Password **\n\nOnly 2 more Attempts Left\n\nTry Again...")

        else:
            print("**Invalid Username and Password**\n\nOnly 2 more Attempts Left\n\nTry Again...")

    elif a == "SIGN UP"  :
        print("will you want to register with us ? \nYES or NO")
        e = input()
        if e == "YES":
            print("WELCOME TO IAS CLUB APP")
            print("       ______________ ")
            print("              |                      / \                    -------")
            print("              |                     /___\                   \ ")
            print("              |                    /     \                   \  ")
            print("       ---------------   ..       /       \    ..      _______\   ")
            print('Fill Your Details\n\n\n1.First Name ')
            f = input()
            print('2.Last Name')
            g = input()
            print('3.D.O.B')
            h = input()
            print("4.Address")
            i = input()
            print("5.Mobile No.")
            j = input()
            print('6.Email Id.')
            k = input()
            print('7.Applying For Which Exam')
            l = input()
            print("Thank you to joining us\n\nUsername & Password Sent to Your Mail id.\n\nCheck it and Sign in")
            print("WELCOME TO IAS CLUB APP")
            print("        ______________ ")
            print("              |                      / \                    ------- ")
            print("              |                     /___\                   \        ")
            print("              |                    /     \                   \       ")
            print("       ---------------   ..       /       \    ..      _______\  \n\n\n\nIf you have already registered with us type :SIGN IN \n\nIf you are new here Type: SIGN UP")
            a = (input())
            list1 = [["Ayush", 100], ["Piyush", 200], ["Neeraj", 300], ["Shraddha", 400]]
            dict1 = dict(list1)

            if a == "SIGN IN":
                print("USERNAME")
                b = str(input())
                print("PASSWORD")
                c = int(input())
                if c == dict1[b]:
                    print("WELCOME", b)
                    print("       ______________ ")
                    print("              |                      / \                    ------- ")
                    print("              |                     /___\                   \        ")
                    print("              |                    /     \                   \       ")
                    print("       ---------------   ..       /       \    ..      _______\       ")

                    print("IAS CLUB\n\n1.Dashboard\n2.Profile\n3.Services\n4.Courses\n5.HELP\n\nWhat you wish to open")
                    d = input()

                    if d == "Profile":
                        print("1.View Profile pic \n2.Edit Profile\n3.Privacy and Security \n4.Language ")
                        z = input('What you wish to open \n')
                        if z == "Edit Profile":
                            print("\n\n**Coming Soon**\n\n")
                            break
                    elif d == "Services":
                        print(
                            "1.Register for UPSC Exam Course\n2.Notes\n3.E-Books\n4.Join Mock Test\n5.Previous Years Paper ")
                    elif d == "Courses":
                        print("\n\n**Coming Soon**\n\n")
                        break
                elif c != dict1[b]:
                    print("Invalid Password **\n\nOnly 2 more Attempts Left\n\nTry Again...")

                else:
                    print("**Invalid Username and Password**\n\nOnly 2 more Attempts Left\n\nTry Again...")



        elif e == "NO":
            print("Thank you ")
            break
    else:
        print('\n\n**INVALID INPUT**\n\nTRY AGAIN...\n\n')
