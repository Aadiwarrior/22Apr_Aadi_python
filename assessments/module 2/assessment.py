from assess_mod import *

def manager():
    while True:
        print("Fruit Market Manager \n\n 1) Add fruit stock \n 2) View fruit stock \n 3) Update Fruit stock \n 4)  exit")
        choice=int(input("Select your choie:"))
        if choice==1:
            addfruitstock()
            
        elif choice==2:
            viewstock()
        else:
            break
while True:
    cs=int(input("\n welcome to fruit market \n \n 1)customer \n 2) Manager \n \n Select your role:"))
    if cs==1:
        pass
    elif cs==2:
        manager()
    else:
        break
