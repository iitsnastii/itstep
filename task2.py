class Eater:
    def __init__(self, food):
        self.favorite_food = food

    def eat(self):
        print(f"Я обожнюю їсти {self.favorite_food}!")


class Sleeper:
    def __init__(self, hours):
        self.sleep_hours = hours

    def sleep(self):
        print(f"Я сплю {self.sleep_hours} годин. ")


class Cat(Eater, Sleeper):

    def __init__(self, food, hours, name):
        Eater.__init__(self, food)
        Sleeper.__init__(self, hours)
        self.name = name
        print(f"Привіт, я кіт {self.name}! ")


murzhyk = Cat(food="рибу", hours=16, name="Мурчик")

murzhyk.eat()
murzhyk.sleep()

print(f"Улюблена їжа Мурчика: {murzhyk.favorite_food}")
print(f"Мурчик спить по: {murzhyk.sleep_hours} годин")