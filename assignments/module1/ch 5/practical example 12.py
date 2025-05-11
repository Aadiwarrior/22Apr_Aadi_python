"""i=int(input("Enter the number of rows:"))
"""
for i in range(1,6):
    for j in range(i):
        print("* ",end="")
    print("")

print("\n")

for i in range (1,6):
    for j in range (1,i+1):
        print(j,end="")
    print("")

print("\n")
for i in range(5,0,-1):
    for j in range(i):
        print("* ",end="")
    print("")

print("\n")

for i in range (5,0,-1):
    for j in range (1,i+1):
        print(j,end="")
    print("")

print("\n")

for i in range (1,6):
    for j in range (i):
        print(chr(j+65),end="")
    print("")
