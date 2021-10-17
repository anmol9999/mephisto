stdDict = {
    'name':'billu',
    'maths':17,
    'english':15,
    'hindi':12,
    'age':14,
    'studies':False,
    'delinquent':True,
    'phone':9393939393
}



# looping dictionary


print('only keys from dictionary in a for loop')

for item in stdDict:
    print(item)

print('only values from dictionary in a for loop')

for item in stdDict:
    print(stdDict[item], end=' ')


print('key and values both from dictionary in a for loop')

for item in stdDict:
    print(item, stdDict[item], end=' ')

print('key and values both from dictionary in a for loop')

# most important method
for k,v in stdDict.items():
    print(k,'=>',v,end=' ')