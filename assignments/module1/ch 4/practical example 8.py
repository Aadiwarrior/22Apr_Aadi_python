age=int(input("Enter your age :"))
bg=input("Enter your blood group to donate it to AB+ :")
w=int(input("Enter your weight:"))
if age>=18:
    if w>=45 and w<=65:
        if bg=="AB+":
            print("You are eligible and you can donate the blood to AB+ blood group people")
        else:
            print("you are eligible but you cannot donate blood to AB+ blood group")
    else:
        print("you are not eligible for donation of blood")
else:
    print("you are not eligible for donation of blood")