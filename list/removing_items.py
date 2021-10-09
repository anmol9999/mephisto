# remove 
# - searching value

colors = ['yellow','green','blue','purple','pink','purple']
colors.remove('yellow')
print(colors)

if 'jellow' in colors:
    colors.remove('jellow')
    print(colors)

if 'pink' in colors:
    colors.remove('pink')
    print(colors)



# pop - removes value by index- if not given idx , it removes last
# the removed item can be stored in a variable

colors.pop(1)
print(colors)

separated_value = colors.pop(2)
print(colors)
print(separated_value)


colors.pop()
print(colors)


# clear - 

colors.clear()
print(colors)