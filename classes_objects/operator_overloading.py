from _typeshed import Self


class shape:

    def __init__(self,w,h):
        self.width = w
        self.height = h

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * self.width * self.height

    def __it__(self,other):
        if self.area() < other.area():
            return True
        return False

    def __repr__(self):
        return str(self.area())


items = [shape(2,2), shape(1,5), shape(3,3), shape(10,10), shape(3,2)]
print(items)

if shape(3,3) > shape(3,2):
    print('yes')

items.sort()
print(items)

        
