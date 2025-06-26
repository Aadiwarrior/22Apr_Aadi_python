import pandas

def billing():
    total=0
    items={}

    while True:
        name=input("Enter food name:")
        price=float(input("Enter the price of your food:"))
        qty=int(input("enter the quantity of your food:"))

        item_total=qty*price
        total += item_total
        items[name]={
            "price": price,
            "quantity": qty,
            "total": item_total
        }
        more=input("Do you want more items (1 for yes and 2 for no):").lower()
        if more !="yes":
            break

    print("\n==========Bill Summary==========\n")
    x=pandas.DataFrame(items)
    print(x)
    print("\n Total Amount: Rs.", total)


billing()

        
