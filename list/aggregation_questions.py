# wap to find the sum of all values in a numerical list
x = [1,23,45,67,89,]
total = 0
for i in x:
    total += i
print(x,'>> total =',total)

# short version

total = sum(x)
print(total)


x_max = max(x)
print(x_max)

x_min = min(x)
print(x_min)


x_mean = sum(x) / len(x)
print(x_mean)