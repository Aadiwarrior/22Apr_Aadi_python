import re

str="I am aadi bavishi"

n=re.search("aadi",str)

if n:
    print("Search found:")
else:
    print("No search found")