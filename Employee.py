from less import Person

class Employee(Person):
    def __init__(self, name, surname, age, year = 1, position=None, salary = 5):
        Person.__init__(self,name,surname,age,year)
        self.position=position
        self.salary=salary


    def income(self,months):
        self.months=months
        return self.salary * months



if __name__=='__main__':
    p=Employee ('Nika','Mili',27)
    print(p.income (2000))


