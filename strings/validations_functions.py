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

if name.startswith("Dr."):
    print("Hello Doctor")
if name.startswith("Mr."):
    print("Hello Mister")

file=input("Enter the filename")
if file.endswith(".exe"):
    print(f"{file} is application file")
elif file.endswith(".doc"):
    print(f"{file} is word file")
elif file.endswith(".pdf"):
    print(f"{file} is PDF file")
elif file.endswith(".png"):
    print(f"{file} is PNG file")
else:
    print(f"{file} is not defined")

