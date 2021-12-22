register_no = input()
a = len(register_no)

if a!=9:
    print("Invalid Id")

elif (register_no[0:2].isdigit() and register_no[2:5].isalpha() and register_no[2:5].isupper() and register_no[5:9].isdigit()):
    print('Valid')

else:
    print("Invalid")
