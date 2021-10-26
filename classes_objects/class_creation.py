# we have to make class for storing information about cake

class Cake:
    brand = "JJ Bakery"
    flavour = "vanilla"
    weight = 2
    is_eggless = False
    color = 'white'


Cake1=Cake()    #onject 1
cake2=Cake()   #object 2

print(Cake1.flavour)



cake2.brand='Chandu bakery'
cake2.is_eggless=False
cake2.flavour='Strawberry'
cake2.color='pink'
cake2.weight=.25

print(cake2.flavour)
print(cake2.is_eggless)

# above written code is :
#   redundant coding
# lengthy lines
#  above problems has  solution -> intro to construction