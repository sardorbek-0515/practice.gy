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

    def make_vois(self):
        print(f"the {self.name} says {self.sound}")  # POLIMORPHISH


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


print("======================== POLIMORPHISH < =============================")
#  POLIMORPHISH  bir hil methodning turli xil shakllari bolishi mumkin
dog.make_vois()
fish.make_vois()

print("--------------")  # biron obj qaysidir classni instins ligini bilish un
# fish > Fish > Animal > object + (isinstance)
# fish > Fish (class) = isinstance hissoblanadi
# fish > Animal (class) = isinstance hissoblanadi
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("Mit", object)
result = a and b and c and d
print(f"natija: {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
