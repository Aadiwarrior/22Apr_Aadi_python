List1 = ('apple', 'banana', 'mango')

for fruit in List1:# It first sees the firs fruit and then the loop starts 
    letter_count=0
    for letter in fruit:
        letter_count+=1
    print(f"The word {fruit} has {letter_count} letters")