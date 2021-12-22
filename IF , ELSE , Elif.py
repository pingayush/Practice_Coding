var1 = 10

var2 = 100                  #var1 and var 2 are integers so we use int variable in var3 to covert string in integer

var3 = int(input())

if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("lesser")
if var3>var1:
    print("Greater")
if var3==var1:
    print("Equal")
else:
    print("Lesser")

list1 = [1,2,3,4,5]
print(4 in list1)
if 4 in list1:
    print("yes")
else:
    print("not in list")
if 6 in list1:
    print("yes")
else:
    print("no")



