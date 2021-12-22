#List,Tuple,Dictionary
#List is dynamic funcition you csn store number,float,string any type of value

a=[10,20,"ajay",True,10.20]
j=0
for i in  a:
    print("A[",j,"]=",i)
    j=j+1

#len funcition
a=[10,20,"ajay",True,10.20]
j=0
for i in range(len(a)):
    print("A[",j,"]=",a[i])
    j=j+1

#append:for adding single element in list
a=[10,20,"ajay",True,10.20]
a.append("shreyash")
print(a)

#for list inside list(nested list)
a=[10,20,"ajay",True,10.20]
p=["shreyash","joshi"]
a.append(p)
print(a)

#for indexing list
a=[10,20,"ajay",True,10.20]
p=["shreyash","joshi"]
a.append(p)
print(a[3][0])
#it will print shreyash
print(a[3][1]
#it will print joshi

#extend:for adding multiple element in list
a=[10,20,"ajay",True,10.20]
p=["shreyash","joshi"]
a.extend(p)
print(a)


#
