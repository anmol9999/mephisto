x = [1,2,3,2,45,45,6,6,7,8,7,9,8,88,78,2,78,9]
print(x)


print( "occurence of 1=",x.count(1))
print( "occurence of 6=",x.count(2))

print( "occurence of 7=",x.count(7))


a = ['chicago','new york','dallas']
b = [12,13,14]
c = ['nevada',57,'texas',46]
print(a)
a.sort()
print(a)

print(b)
b.sort(reverse=True)
print(b)


#print(c)
#c.sort()
#print(c)

y = [1,1,1,1,2,9,2,2,3,3,3,3,3,3]
print(y)
y.reverse()
print(y)


idx = y.index(9)
print('9 found at',idx)
idx = y.index(2)
print('2 found at',idx)


if 99 in y:
    idx = y.index(99)
    print('99 found at',idx)


z = x.copy()
print(z)
print(x)
x.sort()
print(x)
print(z)