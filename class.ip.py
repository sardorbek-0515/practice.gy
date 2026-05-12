''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE  <
    (3) POLIMORPHISH <
'''

print("========================= INHERITENCE  ---  Meros ==========================")
# PERENT > CHILD
# Perent only public & protected properties > (state + method) / ota ugilga uzida bor hislatlarni taqdim qiladi.yani PUBLIC vs Protected bolgan propertylarni
# Farzand Otaning shartni bajaradi


# Perent - ota
class Animal:
    # state
    description = "Bu Class hayvonlarning otasi "

    # constructor
    def __init__(self, voice):
        self.status = "tirik hayvon"
        self.voice = voice
    # method

    def make_vois(self):
        print(f" bu hayvon tovush chiqara oladi:{self.voice}")  # boolin


# Child- bola yaratish
class Dog(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)  # otasiga pass out qilyabdi

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print(" Ha: men sizni himaya qila olaman!")


class Cat(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)  # otasiga pass out qilyabdi

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print(" Ha: men siz bilan o'ynay olaman!")


class Fish(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)  # otasiga pass out qilyabdi

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print(" Ha: suza olaman!")


# Qisqa usul
dog = Dog("Rex", "woow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("----------------------------------")
dog.make_vois()
fish.make_vois()

print("---------------------------------")
print(Animal.description)  # perent orqali
print(Dog.description)  # child orqali


print(dog.voice, fish.voice)  # birga chaqirish
print("dog.status:", dog.status)
print("cat.status:", cat.status)
