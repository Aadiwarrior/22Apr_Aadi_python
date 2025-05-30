def billing():
    total=0
    items=[]

    while True:
        name=input("Enter food name:")
        price=float(input("Enter the pice of your food:"))
        qty=int(input("enter the quantity of your food:"))

        item_total=qty*price
        total += item_total
        items.append((name,qty,price,item_total))
        more=input("Do you want more items (1 for yes and 2 for no):").lower()
        if more !="yes":
            break

    print("\n==========Bill Summary==========\n")
    print("name     price       quantity")

    for item in items:
            name,qty,price,item_total=item
            
            print(f"{name}      {price}     {qty}")
    print("\n Grand Total \n",total)


billing()

        
