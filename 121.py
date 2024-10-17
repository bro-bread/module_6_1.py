
class Animal:
    def __init__(self,name,  alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        self.food = food
        if food.edible == self.food:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")

class Plant:
    def __init__(self,name, edible = False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Fruit(Plant):
    def _frut(self, edible = True):
        edible = self.edible

class Flower(Plant):
    def _frut2(self, edible = True):
        edible = self.edible


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name, 1)
print(p1.name, 2)

print(a1.alive, 3)
print(a2.fed, 4)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)





