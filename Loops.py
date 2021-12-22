list1 = [["ayush",100] ,["piyush",200] , ["neeraj",3000] , ["shraddha",400]]
# print(list1[0] ,  list1[1])

for item  in list1:
    print(item)

for item , car in list1:       #this step is known as iteration.....
    print(item, "have car no.", car)

dict1 = dict(list1)   #thisstep is typecasting from list to dictionary...

print(dict1)

for item in dict1:   #this is printing like dictionary's key...i.e dict1.keys()
    print(item)

dict1 = dict(list1)
print("what's your name sir?")

name = input()

print("sir here is your no. cars")

print(dict1[name])




