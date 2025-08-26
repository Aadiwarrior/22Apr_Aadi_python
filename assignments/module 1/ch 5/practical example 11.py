b=int(input("How many fruits do you want to search?:"))
List1 = ['apple', 'banana', 'mango','orange','watermelon','pear','coconut']
print("Here is the list from which the code will find.")#list is provide using for function and the name is founded by if function
for fruit in List1:
    print(fruit)
for b in range(1,b+1):
    a=input("Enter a fruit name:")
    if a in List1:
        print(f"Founded {a} in the list")
    else:
        print("not found")