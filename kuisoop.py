class Animal:
    name: str
    age: int
    species: str

    def _init_(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


class Cat(Animal):
    def deskripsi(self):
        return '{} adalah kucing berjenis {} yang sudah berumur {} tahun'.format(self.name, self.species, self.age)

    def suara(self):
        return 'meow!'


myCat = Cat()
myCat.name = "Neko"
myCat.age = 3
myCat.species = "Persian"
print(myCat.deskripsi())
print(myCat.suara())
