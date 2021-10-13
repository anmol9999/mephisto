a = {1,2,3}

a.add(23)
a.add("what")
a.add((1,2,3))
print(a)

# you cannot add a list ,dictionary and set in a set

x = [1,2,34,45]
a.update(x)  # adds multiple values to a set
print(a)
