import datetime
stock={}
y=stock
def addfruitstock():
    name=input("Enter the name of the fruit: ")
    qty=(input("enter the qty(in kgs):"))
    price=(input("Enter the price:"))
    fruit={'qty':qty,'price':price}
    stock[name]=fruit
    x=open("assessment file.txt","a")
    x.write(str(datetime.datetime.now())+str(y)+ '\n')
def viewstock():
    print(stock)

