# wap  to add values from user in a set
# they can add any number of values in the set
# use while loop to perform this task


x = set()
while True:
    x = input('enter a value:')
    if not x:
        break
    x.add(x)

print(x)