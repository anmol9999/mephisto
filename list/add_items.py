x = []  #empty list
print('enter 3 values:')

for i in range(3):
    val = input('->')
    x.append(val)

    x.append(10)
    x.append('helium')
    x.append(True)


    x.append(['a','b','c'])  # Append list to the end of list
    print(x)



x.insert(0,200)
x.insert(4,'banana')
x.insert(-3,'apple')
x.insert(2,[1,2,3,4])


print(x)

a = [1,2,3,4]
b = [3,2,3]
print(a)
print(b)

a.extend(b)
print(a)

b.extend(a)
print(b)