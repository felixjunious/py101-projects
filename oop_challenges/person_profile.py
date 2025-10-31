from datetime import date

class Person:
    def __init__(self, fname, lname, byear):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @name.setter
    def name(self, name):
        names = name.strip().split()
        self.first_name = names[0]
        self.last_name = names[1]

    @property
    def age(self):
        year_now = date.today().year
        return year_now - self.birth_year

    def __str__(self):
        return f'Name\t\t: {self.name}\nBirth Year\t: {self.birth_year}\nAge\t\t\t: {self.age}'

if __name__ == '__main__':
    felipe = Person('Felipe', 'Gaviria', 2000)

    print(felipe)

