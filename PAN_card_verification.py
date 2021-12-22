pan_no= input()

l = len(pan_no)

if l != 10:
    print("Invalid no. of characters!!! \n Pan card must be of 9 Characters")

elif (pan_no[0:5].isalpha() and pan_no[0:5].isupper() and pan_no[5:9].isdigit() and pan_no[9].isalpha() and pan_no[9].isupper()):

    print("Valid Pan No.")

else:
    print("Invalid Pan No.")

