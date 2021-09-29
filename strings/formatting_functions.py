# two types of functions
#- that will give output
#  that will change the original variable


name = "we are going to have FUN"

print(name)


uname = name.upper()

print(uname)

lname = name.lower()

print(lname)

n1 = name.capitalize()
print(n1)

n2 = name.title()
print(n2)

n3 = name.swapcase()
print(n3)

n4 = name.casefold()

print(n4)

word = input('what golu does is moan:')

spacing = int(input('select a number for spacing'))
print(f'printing{word} with spacing {spacing}')

lword = word.ljust(spacing)

print(lword)
rword = word.rjust(spacing)
print(rword)
cword = word.center(spacing)
print(cword)

char = input('enter a character')
lword = word.ljust(spacing,char)
print(lword)
rword = word.rjust(spacing,char)
print(rword)
cword = word.center(spacing,char)
print(cword)