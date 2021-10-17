''' wap to create a dict that conntains following sequence 
1:1
2:4
3:9
4:16

...
100 : 10000
hint : use for loop ,not manually
'''

''' wap to sort a dictionary of 5 elemnts.
you can put anything inside the dictionary
'''


dict1 = {}

for i in range(1,100):
    dict1[i] = i**2

print(dict1)


color_dict = {
    'red': '01',
    'blue':'02',
    'green':'03',
    'yellow':'04',
    'black':'05'
}

for key in sorted(color_dict):
    print(key,color_dict[key])


print(dict(sorted(color_dict.items())))