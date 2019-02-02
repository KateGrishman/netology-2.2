# coding=utf-8
class Animal(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.is_hungry = True

    def feed(self):
        self.is_hungry = False


class DairyAnimal(Animal):
    def __init__(self, name, weight, milk_volume):
        super(DairyAnimal, self).__init__(name, weight)
        self.milk_volume = milk_volume

    def get_milk(self):
        if self.milk_volume > 4:
            self.milk_volume -= 4
            return 4
        else:
            return 0


class WoolAnimal(Animal):
    def __init__(self, name, weight, wool_weight):
        super(WoolAnimal, self).__init__(name, weight)
        self.wool_weight = wool_weight

    def shave(self):
        if self.wool_weight > 0:
            w = self.wool_weight
            self.wool_weight = 0
            return w

        raise Exception('Already shaved!')


class Bird(Animal):
    def __init__(self, name, weight, egg_count):
        super(Bird, self).__init__(name, weight)
        self.egg_count = egg_count

    def get_egg(self):
        if self.egg_count > 0:
            self.egg_count -= 1
            return 1
        else:
            return 0


class Duck(Bird):
    def say_smth(self):
        return '{}: knack'.format(self.name)


class Goose(Bird):
    def say_smth(self):
        return '{}: shhhhh'.format(self.name)


class Chicken(Bird):
    def say_smth(self):
        return '{}: ko-ko'.format(self.name)


class Sheep(WoolAnimal):
    def say_smth(self):
        return '{}: baa'.format(self.name)


class Cow(DairyAnimal):
    def say_smth(self):
        return '{}: moo'.format(self.name)


class Goat(DairyAnimal):
    def say_smth(self):
        return '{}: naa'.format(self.name)


egg_count = 0
wool_weight = 0
milk_volume = 0
total_weight = 0

animals = [
    Goose('Серый', 5, 0),
    Goose('Белый', 3, 2),
    Duck('Кряква', 2, 5),
    Sheep('Кудрявый', 55, 10),
    Sheep('Барашек', 100, 20),
    Cow('Манька', 600, 10),
    Goat('Рога', 50, 5),
    Goat('Копыта', 66, 7),
    Chicken('Ко-ко', 1.1, 5),
    Chicken('Кукареку', 1.5, 0),
]

heaviest_animal = animals[0]

for everyone in animals:
    everyone.say_smth()
    everyone.feed()
    if hasattr(everyone, 'get_milk'):
        milk_volume += everyone.get_milk()
    if hasattr(everyone, 'shave'):
        wool_weight += everyone.shave()
    if hasattr(everyone, 'get_egg'):
        egg_count += everyone.get_egg()
    if everyone.weight > heaviest_animal.weight:
        heaviest_animal = everyone

    total_weight += everyone.weight

print(total_weight)
print(heaviest_animal.name)


