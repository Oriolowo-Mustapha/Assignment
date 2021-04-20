num = int(input("Input- "))
divi = num % 3
if divi == 0:
   divi1 = num % 7
   if divi1 == 0:
       print("It is a multiple of 3 and 7")
   else:
        print("It is a multiple of 3 but not a multiple of  7")
    
elif divi > 0:
    divi2 = num % 7
    if divi2 == 0:
        print("It is not a multiple of 3 but a multiple of 7")
    else:
        print("It is not a multiple of 3 or 7")
        
    