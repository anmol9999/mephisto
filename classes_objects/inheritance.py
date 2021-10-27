class item:

    def __init__(self,color,material):
        self.color = color
        self.material = material

# child class
class physicalitem(item):

    def __init__(self,c,m,weight,height,width):
        super().__init__(c,m)
        self.weight = weight
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

#sub class of physical item
class spphysicalitem(physicalitem):

    def __init__(self, c, m, w, h, wd,brand,tech):
        super().__init__(c, m, w, h, wd)
        self.brand = brand
        self.tech = tech


i = item('red','steel')
j = physicalitem('yellow','wood',2,2,4)
k = spphysicalitem('brown','wood',3,2,5,'plywood','anit thermite')

print(j.area(),k.area())