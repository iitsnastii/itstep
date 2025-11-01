class Bowl:
    def __init__(self):
        self.food_amount = 0

class Cat:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.bowl = Bowl()

    def fill_bowl(self):
        self.bowl.food_amount = 100
        print(f"{self.name} насипав повну миску корму.")

    def eat(self):
        if self.bowl.food_amount >= 10:
            self.bowl.food_amount -= 10
            self.satiety += 10
            print(f"{self.name} поїв. Ситість: {self.satiety}")
        else:
            print(f"{self.name} підійшов до миски, але вона порожня!")

    def play(self):
        print(f"{self.name} грається з іграшковою мишкою.")
        self.satiety -= 5
        print(f"Ситість {self.name} впала до {self.satiety}")

murzhyk = Cat(name="Мурчик")
print(f"З'явився кіт {murzhyk.name}!")
print(f"Його ситість: {murzhyk.satiety}")

murzhyk.eat()

murzhyk.fill_bowl()
print(f"Тепер в мисці {murzhyk.bowl.food_amount} корму.")

murzhyk.eat()
print(f"В мисці залишилось: {murzhyk.bowl.food_amount}")

murzhyk.play()

murzhyk.eat()
