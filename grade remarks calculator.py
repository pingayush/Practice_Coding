cgpa=int(input())

if cgpa>=9:
    print("outstanding")
elif  9>cgpa>=8:
    print("excellent")
elif 8>cgpa>=7:
    print("good")
elif 7>cgpa>=6:
    print("average")
elif 6>cgpa>=5:
    print("better")
else:
    print("poor")