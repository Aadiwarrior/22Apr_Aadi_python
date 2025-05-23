city=['Rajkot','Ahmedabad','Surat','Vadodara','Gandhinagar']
print("The cities in the list are:",city)

city.pop()
print("The updated list of cities arter poping is:",city)
b=input("Enter the name of the city you want to remove:")

city.remove(b)
print("The updated list of cities after removing is:",city)