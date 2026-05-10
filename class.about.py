''' CLASS
    (1) What is class
    (2) ordinary vs static properties
    (3)special method
    
'''

print("================ CLASS uzi nima  ==================")
# CLASS lar objct yasash uchun xizmat qiladigan shablon hissoblamnadi
# class - blueprint for object creation !
# static sozini korish bn obj bn emas classni uzi bn keladigan propertylar hisoblanadi


class Person():  # 3ta structurasi bor
    # state
    message = "static class state propert"

    # constructor
    def __init__(self, name, age):  # self bu object
        self.name = name
        self.age = age
        pass

    # method   # harakati  /classni objctlari
    def introduce(self):
        print(f"{self. name} says: How do you do!")

    def say_age(self):
        print(f"{self. name} says I am {self.age} ")
       # static/class method

    @classmethod
    def explain(cls):
        print("static method propert execed!")


person1 = Person("Jack", 24)
person2 = Person("Martin", 35)
person3 = Person("John", 27)

# ordinary state property / odatiy state prpertylari
name = person1.name
print("person1.name:", person1.name)

# ordinary method state / odatiy state propertylar
person1. introduce()
person2.say_age()

print("================ ordinary vs static properties  ==================")
# Static state ishlatganda togridan togri objct bn emas classni uzi bn keladigan statelar message
new_massage = Person.message
print("new_message:", new_massage)


# static method /ishg TUSHIRISH
Person.explain()


print("====================== special method   Maxsus methodlar ni classga boglab organamiz ==============================")
# Pythoning eng kop ishlatadigan maxsusu methodlari
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = "This class makes cars"

   # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):  # start dvigetl ishga tushdi
        print(f"the {self.name} started engine!")

    def stop_engine(self):  # stop dvigetl toxtadi
        print(f"the {self.name} stoped engine!")


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()


print("==================== __new__  =====================")


class Car():
    # state
    description = "This class makes cars"

   # constructor
    def __new__(cls, *args):            # 1- ishga tushadi
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):  # 2- ishga tushadi
        self.name = name
        self.year = year

    # method
    def start_engine(self):  # start dvigetl ishga tushdi
        print(f"the {self.name} started engine!")

    def stop_engine(self):  # stop dvigetl toxtadi
        print(f"the {self.name} stoped engine!")


my_car = Car("Ferrari", 2025)       # 3- ishga tushadi
my_car.start_engine()
my_car.stop_engine()


print("==================== __str__  =====================")


class Car():
    # state
    description = "This class makes cars"

   # constructor
    def __new__(cls, *args):            # 1- ishga tushadi
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):  # 2- ishga tushadi
        self.name = name
        self.year = year

    # method
    def start_engine(self):  # start dvigetl ishga tushdi
        print(f"the {self.name} started engine!")

    def stop_engine(self):  # stop dvigetl toxtadi
        print(f"the {self.name} stoped engine!")

    def __str__(self):  # bunda biz uzimiz xoxlagan narsani yozsak boladi (car_ocj orniga)
        return (f"the car.name: {self.name} was product in {self.year} year")


my_car = Car("Ferrari", 2025)       # 3- ishga tushadi
my_car.start_engine()
my_car.stop_engine()

print("=====")
your_car = Car("Tyoyota", 2026)  # bunning orniga str dan foydalanamiz
print(your_car)


print("==================== __call__ huddi functiondek ishga tushadi  =====================")


class Car():
    # state
    description = "This class makes cars"

   # constructor
    def __new__(cls, *args):            # 1- ishga tushadi
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):  # 2- ishga tushadi
        self.name = name
        self.year = year

    # method
    def start_engine(self):  # start dvigetl ishga tushdi
        print(f"the {self.name} started engine!")

    def stop_engine(self):  # stop dvigetl toxtadi
        print(f"the {self.name} stoped engine!")

    def __str__(self):  # bunda biz uzimiz xoxlagan narsani yozsak boladi (car_ocj orniga)
        return (f"the car.name: {self.name} was product in {self.year} year")

    def __call__(self):
        print("Object call as function!")  # obj function orqali chaqirildi


my_car = Car("Ferrari", 2025)       # 3- ishga tushadi
my_car.start_engine()
my_car.stop_engine()

print("=====")
your_car = Car("Tyoyota", 2026)  # bunning orniga str dan foydalanamiz
print(your_car)
your_car()  # use(call) functiondek ishga tushishini xoxlasak bunda


print("==================== True / False  =====================")


class Car():
    # state
    description = "This class makes cars"

   # constructor
    def __new__(cls, *args):            # 1- ishga tushadi
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):  # 2- ishga tushadi
        self.name = name
        self.year = year

    # method
    def start_engine(self):  # start dvigetl ishga tushdi
        print(f"the {self.name} started engine!")

    def stop_engine(self):  # stop dvigetl toxtadi
        print(f"the {self.name} stoped engine!")

    def __str__(self):  # bunda biz uzimiz xoxlagan narsani yozsak boladi (car_ocj orniga)
        return (f"the car.name: {self.name} was product in {self.year} year")

    def __call__(self):
        print("Object call as function!")  # obj function orqali chaqirildi
        return True


my_car = Car("Ferrari", 2025)       # 3- ishga tushadi
my_car.start_engine()
my_car.stop_engine()

print("=====")
your_car = Car("Tyoyota", 2026)  # bunning orniga str dan foydalanamiz
print(your_car)
response = your_car()  # use(call) functiondek ishga tushishini xoxlasak bunda/tru,false
print("response:",  response)
