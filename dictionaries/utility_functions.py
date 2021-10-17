marks = {
    'rohan':2,
    'rehan':3,
    'sohan':4,
    'mohan':9,
    'ali':8,
    
}

names = list(marks.keys())
print(names)

numbers = list(marks.values())
print(numbers)

items = list(marks.items())
print(items)

a = 'ramu'
b ='lalita'
c = 'shamu'
d ='sushma'
e = 'jaay'

default_marks = 'N/A'




new_students = dict.fromkeys([a,b,c,d,e],default_marks)
print(new_students)

positions = list(range(1,11))
positions_dict = dict.fromkeys(positions,"available")
print(positions_dict)


copy_of_dict = positions_dict.copy()
print(copy_of_dict)