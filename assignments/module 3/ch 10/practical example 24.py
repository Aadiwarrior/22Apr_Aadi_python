import re

str="I am aadi bavishi"

n=re.match("aadi",str)

if n:
    print("match found:")
else:
    print("No match found")