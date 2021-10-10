'''comprehension:
- when we want to create a list from an existing list in one line
- mapping-> generate same size sequence from existing sequence
- filtering-> create a smaller sequence from existing one,using a condition
'''

'''syntax

newlist = [ operation loop- for existing list `condition`]

'''




x = [2,24,56,7,87,189,13]
# mapping

x2 = [i**2 for i in x ]
print(x)
print(x2)

x3 = [i**2+10 for i in x ]
print(x)
print(x3)

# filter
x_odd = [i for i in x if i%2!=0]
print(x_odd)

x_odd_sqr = [i**2 for i in x if i%2!=0]
print(x_odd_sqr)
