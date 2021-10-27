class Movie:

    def __init__(self,name,genre,year):
        self.name = name  # instance variable
        self.genre = genre
        self.year = year

    def show(self):
        print('details:',self.name,"/".join(self.genre),self.year)


m = Movie('Free guy',['comedy','action'],2021)
m2 = Movie("Dune",['sci fi','drama'],2021)

m.show()
m2.show()