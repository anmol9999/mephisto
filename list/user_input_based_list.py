# wap to take user input to create a list
# the user should decide the size of list
# the list should be numeric
# display list values and sum ,min,max,mean of the list

x = []
limit =int(input('enter size of list'))





for i in range(limit):
    val = int(input(f'{i+1}'))
    x.append(val)

print('enter three values:')


print('numbers')
print('sum',sum(x))




