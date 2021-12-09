def greatest(a,b,c):
    if a>b:
        if a>c:
            print("A is greatest")
        else:
            print("C is greatest")
    elif b>c:
        print("B is greatest")
     
    else:
        print("C is greatest")
        


greatest(2,3,4)
greatest(5,8,7)
greatest(10,2,30)

================================================
Dry Run:


Example-1:
    greatest(2,3,4)
    2<3 ----------------------------> Loop-1 Failed
    2<4------------------------------>Loop-2 Failed
              *Loop-3 will Run*
    Hence:
        "C is greatest"

Example-2:
    greatest(5,8,7)
    5<8 ------------------------------> Loop-1 Failed
    8>7 -------------------------------> Loop-2 will Run
    
    Hence:
        "B is greatest"

Example-3:
    greatest(10,2,30)
    10>2 --------------------------------> Loop-1 will Run
    10<30 ---------------------------------------> Loop-1(a) Failed
              *Loop-1(b) will Run*
    Hence:
        "C is greatest"
