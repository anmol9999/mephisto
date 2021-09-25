#mathematical
#condition
#assignment
#logical
#membership
#instance

a = 10*3
print(a)
a = 10/3   #division real no
print(a)
a = 10//3 #integer division
print(a)
a = 10%3 #modulus remainder
print(a)
a = 10**3 #exponent
print(a)
a = 10+3
print(a)
a = 10-3
print(a)

#comparison operator
a = 10
b = 3
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a  == b)
print(a !=b)


#assignment operator

c = 15
print(c)

c += 10 #add 10 to exixsting value of c
print(c)
c -= 10 #subtract 10 from existing value of c
print(c)
c *= 10
print(c)
c /= 10
print(c)
c //= 10
print(c)
c %= 10
print(c)
c **= 10 
print(c)

#logical operator - multiple expression

a = 5
b = 15
c = 10
print( a > b and a > c)
print( b > a or b > 100)
print( not a > b)
print(a > b and a < c or a > 10)
print( not a > b and a < c or a > 10)
 
# membership operator - in membership op[ it can search a value in a iterable]
colors = ['red','blue','green','purple','yellow']

print('red' in colors)
print('brown' in colors)
print('orange' in colors )
print('45' in colors)