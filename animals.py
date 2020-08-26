class Creature:
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        animal.update({name: weight})

    def feed(self):
        print(f'{self.name} накормлен(а)')

    def sound(self):
        print(f'{self.name} говорит {self.voice}')


class Birds(Creature):
    def collect_eggs(self):
        print('Яйца собраны')


class Animals(Creature):
    pass


class MilkyWay(Animals):
    def get_milk(self):
        print('Молоко собрано')


class Goose(Birds):
    creature_type = 'Гусь'
    voice = 'га-га-га'

    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color


class Chicken(Birds):
    creature_type = 'Курица'
    voice = 'ко-ко-ко'


class Duck(Birds):
    creature_type = 'Утка'
    voice = 'кря-кря-кря'


class Cow(MilkyWay):
    creature_type = 'Корова'
    voice = 'Муууу'


class Sheep(Animals):
    creature_type = 'Овца'
    voice = 'Беее'

    def cut_wool(self):
        print('Шерсть сострижена')


class Goat(MilkyWay):
    creature_type = 'Коза'
    voice = 'Меее'


animal = {}

goose1 = Goose('Серый', 50, 'серый')
goose2 = Goose('Белый', 55, 'белый')
chicken1 = Chicken('Ко-ко', 40)
chicken2 = Chicken('Кукареку', 45)
duck1 = Duck('Кряква', 20)
sheep1 = Sheep('Барашек', 90)
sheep2 = Sheep('Кудрявый', 95)
cow1 = Cow('Манька', 160)
goat1 = Goat('Рога', 70)
goat2 = Goat('Копыта', 75)

goose1.collect_eggs()
chicken1.collect_eggs()
sheep1.cut_wool()
cow1.get_milk()
goat1.get_milk()
cow1.feed()
cow1.sound()

total_weight = 0
max_weight = int(max(animal.values()))
for name, weight in animal.items():
    total_weight += int(weight)
    if int(weight) == max_weight:
        print(f'\nСамое тяжелое животное - {name}, {weight} кг')
print(f'Общий вес всех животных - {total_weight} кг')