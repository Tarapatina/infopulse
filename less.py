class Person:
    desk = 'lala'

    def __init__(self, name, surname, age, year = 1):
        self.name = name
        self.age = age
        self.surname = surname
        self.year = year


#    def set_name(self, name, surname):
#       self.ful_name = [name,surname]


    def full_name(self):
        return self.name + ' '+self.surname


    def get_older(self, year):
        self.age += year



if __name__=='__main__':
    p = Person('Nika','Klar',27)
    p.name='katti'
    print(p.full_name(),p.get_older(2))
    print(p.age)

