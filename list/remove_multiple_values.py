x = [1,2,3,2,45,45,6,6,7,8,7,9,8,88,78,2,78,9]

print(x)
y = x.copy()


# remove all the 6sfrom list



for i in range(x.count(6)):
    x.remove(6)


print('removed all 6s')
print(x)
  

  # alternative method

while True:
    idx = y.index(2)
    y.pop(idx)
    print(y)