value = input('enter something')


ans = value.isupper()
print('is the value entered is Upper?', ans)


ans = value.islower()
print('is the value entered is lower?', ans)

ans = value.isalpha()
print('does the value contains only alphabets?', ans)

ans = value.isnumeric()

print('does the value contains only numbers?', ans)

ans = value.isspace()
print('does the value contains only space?', ans)

ans = value.isprintable()
print('is the value printable on screen?', ans)

ans = value.isdigit()
print('does the value contains only digits?, ans')

ans = value.decimal()
print('does the value contains decima number?, ans')


name = 'dr. ram verma'

if name.startswith('dr'):
    print('hello doctor')
if name.startswith('mr'):
    print('hello mister')

file = input('enter the filename:')
if file.endswith('.exe'):
    print(f'{file}is application file')
elif file.endswith('.doc'):
    elif file.endswith('.doc'):
elif file.endswith('.pdf'):

