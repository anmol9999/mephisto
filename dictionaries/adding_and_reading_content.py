words = {}     # blank dictionary


words['alpha'] = " number one,the starting value,or the top value"
print("user input-->")


# taking input from user

for i in range(3):
    k = input('enter a word-->')
    v = input('enter a meaning-->')
    words[k] = v


print(words)


# reading a particular value

print(words['alpha'])

# another way of finding value
print(words.get('alpha'))


print(words['beta'])                         #           will give an error cause beta does not exist



print(words.get('beta','not found 😢'))
