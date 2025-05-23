city=['Rajkot','Ahmedabad','Surat','Vadodara','Gandhinagar']
print("The cities in the list are:",city)
a=input("Enter the name of the city you want to append:")
city.append(a)
print("The updated list of cities is:",city)
b=input("Enter the name of the city you want to insert:")
c=int(input("Enter the index at which you want to insert the city:"))
city.insert(c,b)
print("The updated list of cities after insertion is:",city)