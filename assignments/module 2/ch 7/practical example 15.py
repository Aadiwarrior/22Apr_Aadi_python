dict={"id":'114034','name':'aadi bavishi','city':'rajkot','state':'gujarat','country':'India','sub':'python'}
print('the dictionary is',dict)
a=input('Enter the key whose value you want to change:')
b=input('Enter the value of the key:')
for i in dict:
    if i==a:
        dict[a]=b
        print("the updated dictionary is:" ,dict)
    else:
        print('The key is not in the dictionary')