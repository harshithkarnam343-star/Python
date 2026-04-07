
num = 3
attempts = 0 

while True :
    a = int(input("Enter ur guess : "))
    if (a == num ):
        print("Correct in ", attempts,"tries!!")
        attempts += 1
        
    else :
        print("Try again ")
        break 