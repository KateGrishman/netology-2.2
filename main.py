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


goose_grey = Goose('Серый', 5, 0)
goose_grey.feed()
egg_count += goose_grey.get_egg()
total_weight += goose_grey.weight
heaviest_animal = goose_grey
print(goose_grey.say_smth())

goose_white = Goose('Белый', 3, 2)
goose_white.feed()
egg_count += goose_white.get_egg()
total_weight += goose_white.weight
if goose_white.weight > heaviest_animal.weight:
    heaviest_animal = goose_white
print(goose_white.say_smth())

duck = Duck('Кряква', 2, 5)
duck.feed()
egg_count += duck.get_egg()
total_weight += duck.weight
if duck.weight > heaviest_animal.weight:
    heaviest_animal = duck
print(duck.say_smth())

sheep_curl = Sheep('Кудрявый', 55, 10)
sheep_curl.feed()
wool_weight += sheep_curl.shave()
total_weight += sheep_curl.weight
if sheep_curl.weight > heaviest_animal.weight:
    heaviest_animal = sheep_curl
print(sheep_curl.say_smth())

sheep_sheep = Sheep('Барашек', 100, 20)
sheep_sheep.feed()
wool_weight += sheep_sheep.shave()
total_weight += sheep_sheep.weight
if sheep_sheep.weight > heaviest_animal.weight:
    heaviest_animal = sheep_sheep
print(sheep_sheep.say_smth())

cow = Cow('Манька', 600, 10)
cow.feed()
milk_volume += cow.get_milk()
total_weight += cow.weight
if cow.weight > heaviest_animal.weight:
    heaviest_animal = cow
print(cow.say_smth())

goat_horn = Goat('Рога', 50, 5)
goat_horn.feed()
milk_volume += goat_horn.get_milk()
total_weight += goat_horn.weight
if goat_horn.weight > heaviest_animal.weight:
    heaviest_animal = goat_horn
print(goat_horn.say_smth())

goat_hoof = Goat('Копыта', 66, 7)
goat_hoof.feed()
milk_volume += goat_hoof.get_milk()
total_weight += goat_hoof.weight
if goat_hoof.weight > heaviest_animal.weight:
    heaviest_animal = goat_hoof
print(goat_hoof.say_smth())

chiken_ko = Chicken('Ко-ко', 1.1, 5)
chiken_ko.feed()
egg_count += chiken_ko.get_egg()
total_weight += chiken_ko.weight
if chiken_ko.weight > heaviest_animal.weight:
    heaviest_animal = chiken_ko
print(chiken_ko.say_smth())

chiken_cock = Chicken('Кукареку', 1.5, 0)
chiken_cock.feed()
egg_count += chiken_cock.get_egg()
total_weight += chiken_cock.weight
if chiken_cock.weight > heaviest_animal.weight:
    heaviest_animal = chiken_cock
print(chiken_cock.say_smth())

print(total_weight)
print(heaviest_animal.name)
