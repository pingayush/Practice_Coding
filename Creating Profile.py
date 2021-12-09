print("WELCOME TO IAS CLUB APP")
print("       ______________ ")
print("              |                      / \                    ------- ")
print("              |                     /___\                   \        ")
print("              |                    /     \                   \       ")
print("       ---------------   ..       /       \    ..      _______\  \n\n\n\nIf you have already registered with us type :SIGN IN \n\nIf you are new here Type: SIGN UP     ")



a=(input())

if a == "SIGN IN":
    print("USERNAME")
    b=(input())
    print("PASSWORD")
    C=input()

    print("       ______________ ")
    print("              |                      / \                    ------- ")
    print("              |                     /___\                   \        ")
    print("              |                    /     \                   \       ")
    print("       ---------------   ..       /       \    ..      _______\       ")





    print("IAS CLUB\n\n1.Dashboard\n2.Profile\n3.Services\n4.Courses\n5.HELP\n\nWhat you wish to open")
    d=input()


    if d=="Profile":
        print("1.View Profile pic \n2.Edit Profile\n3.Privacy and Security \n4.Language ")
    elif d== "Services":
        print("1.Register for UPSC Exam Course\n2.Notes\n3.E-Books\n4.Join Mock Test\n5.Previous Years Paper  ")



elif a == "SIGN UP":
    print("will you want to register with us ? \nYES or NO")
    e=input()
    if e=="YES":
        print("WELCOME TO IAS CLUB APP")
        print("       ______________ ")
        print("              |                      / \                    ------- ")
        print("              |                     /___\                   \        ")
        print("              |                    /     \                   \       ")
        print("       ---------------   ..       /       \    ..      _______\       ")
        print('Fill Your Details\n\n\n1.First Name ')
        f=input()
        print('2.Last Name')
        g=input()
        print('3.D.O.B')
        h=input()
        print("4.Qalifications")
else:
    print('Sorry please try to answer from the choices that we have given to you')




