age=int(input("Enter your age :"))
bg=input("Enter your blood group :")
w=int(input("Enter your weight:"))
if age>=18:
    if w>=45 and w<=65:
        if bg=="AB+":
            print("You are eligible for donation of blood to many people")
        else:
            print("you are eligible but to a fewer section of people")
    else:
        print("you are not eligible for donation of blood")
else:
    print("you are not eligible for donation of blood")