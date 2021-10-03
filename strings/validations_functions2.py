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

