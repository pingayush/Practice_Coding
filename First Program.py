science=int(input("Enter the value for Science"))
math=int(input("Math"))
english=int(input("English"))
hindi=int(input("Hindi"))
socialscience=int(input("SocialScience"))
total=(science+math+english+hindi+socialscience)
per=total//5
if(per>=90):
     print("Outstanding")
elif(per>60):
     print("Ist Division")             
elif(per>50):
     print("Failed")
           
