i=2
while(i>0):
    age_1 = int(input("Enter The Age Of First Person. \n"))
    age_2 = int(input("Enter The Age Of Second Person. \n"))
    age_3 = int(input("Enter The Age Of Third Person. \n"))

    if age_1 < age_2 and age_1 < age_3:
        print("First student is youngest")
    elif age_2 < age_3 and age_2 < age_1:
        print("Second Student Is The Youngest")
    elif age_3 < age_1 and age_3 < age_2:
        print("Third Student Is The Youngest.")
    if age_1 == age_2:
        if age_1 < age_3:
            print("Students First & Second are yougest")
    if age_2 == age_3:
        if age_2 < age_1:
            print("Students Second & Third are yougest")
    if age_1 == age_3:
        if age_1 < age_2:
            print("Students First & Third are yougest")
    if age_2 == age_3 == age_1:
        print("All Students Have The Same Age.")
    print("\n\n   **NEXT CASE**   \n\n")


